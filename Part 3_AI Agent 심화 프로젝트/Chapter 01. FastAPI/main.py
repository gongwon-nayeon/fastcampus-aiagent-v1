from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Annotated, Dict, Any, List
from typing_extensions import TypedDict

from fastapi import FastAPI
from fastapi.responses import StreamingResponse, JSONResponse

from dotenv import load_dotenv
import os

load_dotenv()
os.getenv("OPENAI_API_KEY")
os.environ["USER_AGENT"] = "myagent"

# ----------------------------
# 1. FastAPI Setup
# ----------------------------

app = FastAPI()


@app.get("/")
async def root():
    return "Hello World"


# ----------------------------
# 2. Define State and Graph
# ----------------------------

from langchain_community.document_loaders import WebBaseLoader
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages

from langgraph.prebuilt import tools_condition, ToolNode


class State(TypedDict):
    messages: Annotated[list, add_messages]


graph_builder = StateGraph(State)

llm = ChatOpenAI(model="gpt-4o")


@tool
def scrape_webpages(urls: List[str]) -> str:
    """Use requests and bs4 to scrape the provided web pages for detailed information."""
    loader = WebBaseLoader(urls)
    docs = loader.load()
    return "\n\n".join(
        [
            f'<Document name="{doc.metadata.get("title", "")}">\n{doc.page_content}\n</Document>'
            for doc in docs
        ]
    )


async def chatbot(state: State):
    llm_with_tools = llm.bind_tools([scrape_webpages])
    response = await llm_with_tools.ainvoke(state["messages"])
    return {"messages": [response]}


graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")

web_scraper_node = ToolNode([scrape_webpages], name="web_scraper")
graph_builder.add_node("web_scraper", web_scraper_node)

graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition,
    {
        "tools": "web_scraper",
        END: END,
    },
)

graph_builder.set_entry_point("chatbot")
graph_builder.add_edge("web_scraper", "chatbot")

graph = graph_builder.compile()

# ----------------------------
# 3. FastAPI Endpoint
# ----------------------------


class UserInput(BaseModel):
    message: str


@app.post("/ai-assist/invoke")
async def invoke(user_input: UserInput):
    try:
        response = await graph.ainvoke(
            {"messages": [HumanMessage(content=user_input.message)]}
        )
        final_message = response["messages"][-1]
        return JSONResponse(
            content={"content": final_message.content},
            media_type="application/json; charset=utf-8",
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/ai-assist/stream")
async def stream(message: str = ""):
    async def event_generator():
        import json

        async for chunk in graph.astream({"messages": [HumanMessage(content=message)]}):
            try:
                serializable_chunk = {}
                for key, value in chunk.items():
                    serializable_chunk[key] = value["messages"][0].content
                yield f"[Node update] {json.dumps(serializable_chunk, ensure_ascii=False)}\n\n"
            except Exception as e:
                yield f"Error processing chunk: {str(e)}\n\n"

    return StreamingResponse(
        event_generator(), media_type="text/event-stream; charset=utf-8"
    )

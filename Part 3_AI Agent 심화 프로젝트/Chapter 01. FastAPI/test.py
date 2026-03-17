from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
async def root():
    return "Hello, World!"


@app.get("/test")
async def test():
    return {"message": "Hello, FastAPI!"}


# GET : 서버에 저장된 데이터를 요청할 때 사용
# POST : 새로운 데이터를 서버에 보낼 때, 저장할 때 사용
# PUT : 기존 데이터를 수정할 때(덮어쓸때) 사용
# DELETE : 서버에 저장되어 있는 특정 데이터를 삭제할 때 사용

messages = {}


@app.post("/message")
async def post_message(message: str):
    return {"message": message}


@app.put("/message/{message_id}")
async def put_message(message_id: int, new_message: str):
    messages[message_id] = new_message
    return {"message": f"Message {message_id} updated to '{new_message}"}


@app.delete("/message/{message_id}")
async def delete_message(message_id: int):
    if message_id not in messages:
        return HTTPException(status_code=404, detail="Message not found")
    del messages[message_id]
    return {"message": f"Message {message_id} deleted"}

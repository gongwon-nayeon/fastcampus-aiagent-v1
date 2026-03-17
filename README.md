# 패스트캠퍼스 **🚀 실전 AI Agent의 모든 것 : 34개 프로젝트로 MCP부터 GraphRAG Agent까지 (by.공원나연)**

※ 본 레포지토리는 LangChain v1 최신 버전을 반영하여 [기존 실습 코드](https://github.com/gongwon-nayeon/fastcampus-aiagent)를 마이그레이션한 레포지토리입니다.
변경된 사항은 코드 속 주석 혹은 마크다운 셀로 기록해두었으며, 궁금한 점이 있다면 패스트캠퍼스 커뮤니티 질문 공간을 활용해주세요. 감사합니다 🙇

Python version: 3.13.5

```
📦fastcampus-aiagent
 ┣ 📂Part 1_AI Agent 이해와 입문 프로젝트
 ┃ ┣ 📂Chapter 02. LangGraph 기초다지기
 ┃ ┗ 📂Chapter 03. LangGraph 입문 프로젝트
 ┣ 📂Part 2_AI Agent 활용 프로젝트
 ┃ ┣ 📂Chapter 01. 반복하고 수정하는 Agent
 ┃ ┣ 📂Chapter 02. 컨텍스트 품질을 보장하는 RAG
 ┃ ┣ 📂Chapter 03. N개 이상의 Agent
 ┃ ┗ 📂Chapter 04. 사전구축 Agent
 ┣ 📂Part 3_AI Agent 심화 프로젝트
 ┃ ┣ 📂Chapter 01. FastAPI
 ┃ ┣ 📂Chapter 02. 추천시스템 Agent
 ┃ ┗ 📂Chapter 03. GraphRAG
 ┗ 📜README.md
 ```

---

📍 본 레포지토리는 패스트캠퍼스 **🚀 실전 AI Agent의 모든 것 : 34개 프로젝트로 MCP부터 GraphRAG Agent까지 (by.공원나연)** 강의의 실습 코드입니다.

👉 https://fastcampus.co.kr/data_online_graphrag


---

## 실습 환경 설정

### 사전 요구사항

- Python 3.11 이상
- OpenAI API Key (https://platform.openai.com/api-keys)

### 1. uv 설치

#### Windows (PowerShell)

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### macOS / Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

### 2. 가상환경 생성 및 패키지 설치

#### 방법 1: uv sync 사용 (권장)

```bash
# pyproject.toml을 기반으로 가상환경 생성 및 패키지 설치
uv sync

# 가상환경 활성화 (Windows)
.venv\Scripts\activate

# 가상환경 활성화 (macOS/Linux)
source .venv/bin/activate
```

#### 방법 2: requirements.txt 사용

```bash
# 가상환경 생성
uv venv

# 가상환경 활성화 (Windows)
.venv\Scripts\activate

# 가상환경 활성화 (macOS/Linux)
source .venv/bin/activate

# 패키지 설치
uv pip install -r requirements.txt
```

---

### 3. Jupyter Notebook 커널 등록

VS Code에서 Jupyter Notebook을 사용하려면 커널을 등록해야 합니다.

#### Windows

```powershell
.venv\Scripts\python.exe -m ipykernel install --user --name=fastcampus-aiagent --display-name="fastcampus-aiagent"
```

#### macOS/Linux

```bash
.venv/bin/python -m ipykernel install --user --name=fastcampus-aiagent --display-name="fastcampus-aiagent"
```

커널 등록 후 **VS Code를 리로드**하면 노트북에서 "llm Day1" 커널을 선택할 수 있습니다.

---

### 4. 환경변수 설정

`.env.example` 파일을 `.env`로 복사하고 본인의 API 키를 입력하세요.

#### Windows (PowerShell)

```powershell
Copy-Item .env.example .env
```

#### macOS/Linux

```bash
cp .env.example .env
```

`.env` 파일을 열고 다음과 같이 수정:

```
OPENAI_API_KEY=your_openai_api_key_here
```

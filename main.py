from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from typing import List
from datetime import datetime
from pydantic import BaseModel
import pymongo
import uuid
from fastapi.responses import JSONResponse

app = FastAPI()

# 跨域
origins = [
    "http://localhost:8081",  # 前端跨域
    "http://localhost",       # 通配本地开发
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 连接到MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["AntiEmo"]  # 选择数据库
clt = db["conversation"]  # 选择集合


class Message:
    user_id: int
    text: str
# 一次问答
class Conversation(BaseModel):
    input: str
    output: str
    timestamp: str
# 多轮问答
class ChatSession(BaseModel):
    user_id: str
    session_id: str
    conversations: List[Conversation]
class ChatRequest(BaseModel):
    user_id: str
    session_id: str
    text: str

# 开始新会话或追加对话
@app.post("/chat")
async def chat(request: ChatRequest):
    user_id = request.user_id
    session_id = request.session_id
    text = request.text
    # # 上下文支持
    # context = clt.find_one({"session_id": session_id, "user_id": user_id})["conversations"]
    # prompt = "\n".join([f"用户: {c['input']}\n模型: {c['output']}" for c in context]) + f"\n用户: {text}"

    # 模拟大模型回复
    response = "大模型回复: " + text  # 替换为真实大模型调用
    new_conversation = {
        "input": text,
        "output": response,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

    # 检查会话是否存在
    session = clt.find_one({"session_id": session_id, "user_id": user_id})
    if session:
        # 如果有该会话则追加到现有会话
        clt.update_one(
            {"session_id": session_id},
            {"$push": {"conversations": new_conversation}, "$set": {"end_time": datetime.utcnow().isoformat() + "Z"}}
        )
    else:
        # 创建新会话
        new_session = {
            "user_id": user_id,
            "session_id": session_id,
            "start_time": datetime.utcnow().isoformat() + "Z",
            "end_time": datetime.utcnow().isoformat() + "Z",
            "model_version": "ChatGlm3_6b",
            "language": "zh",
            "conversations": [new_conversation],
            "status": "active"
        }
        clt.insert_one(new_session)

    return {"response": response}

# 生成唯一 session_id 的接口
@app.get("/generate/id")
async def generate_id():
    session_id = str(uuid.uuid4())  # 生成 UUID 作为 session_id
    print(session_id)
    return {"data": session_id}

# 生成标题
@app.get("/chat/title/{session_id}")
async def generate_title(session_id: str):
    # 模拟生成标题（替换为真实逻辑）
    title = f"Conversation {session_id}"  # 示例标题
    return JSONResponse(content={"title": title})

# 查询会话历史
@app.get("/history/{user_id}/{session_id}")
async def get_history(user_id: str, session_id: str):
    session = clt.find_one({"user_id": user_id, "session_id": session_id})
    if session:
        return {"conversations": session["conversations"]}
    return {"error": "Session not found"}

@app.post("/chat/repeat")
async def chat(request: ChatRequest):
    user_id = request.user_id
    session_id = request.session_id
    text = request.text

@app.get("/")
async def root():

    return {"resul"}  # 返回一个字典，包含查询结果


# 关闭 MongoDB 连接
@app.on_event("shutdown")
def shutdown_db_client():
    client.close()
    print("MongoDB 连接已关闭")
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# 创建 FastAPI 应用实例
app = FastAPI(title="用户管理 API", version="1.0.0")


# 定义用户注册请求模型
class UserRegisterRequest(BaseModel):
    username: str
    email: EmailStr


# 定义用户响应模型
class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime


# 模拟数据库（实际项目中应使用真实数据库）
users_db = []
current_id = 1


@app.post("/users/", response_model=UserResponse)
async def register_user(user_data: UserRegisterRequest):
    """
    用户注册接口
    FastAPI 自动验证请求数据并生成 API 文档
    """
    global current_id

    # 模拟保存用户到数据库
    user = UserResponse(
        id=current_id,
        username=user_data.username,
        email=user_data.email,
        created_at=datetime.now(),
    )

    users_db.append(user)
    current_id += 1

    return user


@app.get("/users/", response_model=list[UserResponse])
async def list_users():
    """获取所有用户列表"""
    return users_db


@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    """根据 ID 获取用户信息"""
    for user in users_db:
        if user.id == user_id:
            return user
    return {"error": "用户不存在"}

from typing import NewType

# 创建语义不同的类型
UserId = NewType("UserId", int)
PostId = NewType("PostId", int)
Email = NewType("Email", str)


def get_user_profile(user_id: UserId) -> dict:
    return {"user_id": user_id, "name": "小白"}


def get_post_content(post_id: PostId) -> str:
    return f"Content of post {post_id}"


# 使用时需要显式转换
raw_id = 123
user_id = UserId(raw_id)
post_id = PostId(raw_id)

# 类型检查通过
user_data = get_user_profile(user_id)
post_content = get_post_content(post_id)

# 类型错误！期望 UserId，传入 PostId
user_data = get_user_profile(post_id)  # 代码能运行，但类型检查器会报错
print(user_data)

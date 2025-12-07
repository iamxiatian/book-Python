from typing import Protocol


class Database(Protocol):
    def save_user(self, user_data: dict) -> None: ...


class PostgreSQLDatabase:
    def save_user(self, user_data: dict) -> None:
        print(f"PostgreSQL: 保存用户 {user_data}")


class InMemoryDatabase:
    def save_user(self, user_data: dict) -> None:
        print(f"内存数据库: 保存用户 {user_data}")


class UserService:
    def __init__(self, database: Database):
        # 依赖抽象，而不是具体实现
        self.database = database

    def create_user(self, username: str, email: str) -> None:
        user_data = {"username": username, "email": email}
        self.database.save_user(user_data)

# 测试 DIP
def test_dip():
    # 使用不同的数据库实现
    postgres_db = PostgreSQLDatabase()
    memory_db = InMemoryDatabase()

    service1 = UserService(postgres_db)
    service1.create_user("小非", "xiaofei@example.com")

    service2 = UserService(memory_db)
    service2.create_user("小白", "xiaobai@example.com")


test_dip()

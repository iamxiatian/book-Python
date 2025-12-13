class UserManager:
    """上帝类 - 负责太多事情"""

    def __init__(self):
        self.users = []

    def add_user(self, username: str, email: str) -> None:
        """添加用户"""
        # 验证逻辑
        if not self._is_valid_email(email):
            raise ValueError("无效的邮箱地址")

        # 业务逻辑
        user = {"username": username, "email": email}
        self.users.append(user)

        # 日志记录
        self._log_user_creation(username)

        # 数据持久化
        self._save_to_database(user)

    def _is_valid_email(self, email: str) -> bool:
        return "@" in email

    def _log_user_creation(self, username: str) -> None:
        print(f"用户 {username} 已创建")

    def _save_to_database(self, user: dict) -> None:
        print(f"保存用户到数据库: {user}")


# 遵循 SRP 的重构：每个类只承担一项明确职责
class EmailValidator:
    """专门负责邮箱验证"""

    def is_valid(self, email: str) -> bool:
        return "@" in email and "." in email


class UserLogger:
    """专门负责用户相关日志"""

    def log_creation(self, username: str) -> None:
        print(f"用户 {username} 已创建")


class UserRepository:
    """专门负责用户数据持久化"""

    def save(self, user: dict) -> None:
        print(f"保存用户到数据库: {user}")


class UserService:
    """专门负责用户业务逻辑"""

    def __init__(self):
        self.validator = EmailValidator()
        self.logger = UserLogger()
        self.repository = UserRepository()
        self.users = []

    def add_user(self, username: str, email: str) -> None:
        """添加用户 - 只关注业务逻辑"""
        if not self.validator.is_valid(email):
            raise ValueError("无效的邮箱地址")

        user = {"username": username, "email": email}
        self.users.append(user)
        self.logger.log_creation(username)
        self.repository.save(user)


# 测试 SRP 重构
def test_srp():
    print("=== 重构前 ===")
    manager = UserManager()
    try:
        manager.add_user("Alice", "alice@example.com")
    except Exception as e:
        print(f"错误: {e}")

    print("\n=== 重构后 ===")
    service = UserService()
    try:
        service.add_user("Bob", "bob@example.com")
    except Exception as e:
        print(f"错误: {e}")


test_srp()

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


# 依赖注入容器示例
class DependencyContainer:
    """简单的依赖注入容器"""

    def __init__(self):
        self._dependencies = {}

    def register(self, interface: type, implementation: type):
        self._dependencies[interface] = implementation

    def resolve(self, interface: type):
        impl_class = self._dependencies.get(interface)
        if not impl_class:
            raise ValueError(f"未注册的依赖: {interface}")
        return impl_class()


# 更复杂的依赖注入示例
class EmailService(Protocol):
    def send_welcome_email(self, email: str) -> None: ...


class SMTPEmailService:
    def send_welcome_email(self, email: str) -> None:
        print(f"SMTP: 发送欢迎邮件到 {email}")


class SendGridEmailService:
    def send_welcome_email(self, email: str) -> None:
        print(f"SendGrid: 发送欢迎邮件到 {email}")


class NotificationService(Protocol):
    def notify_user_created(self, username: str) -> None: ...


class AdvancedUserService:
    def __init__(
        self,
        database: Database,
        email_service: EmailService,
        notification_service: NotificationService,
    ):
        self.database = database
        self.email_service = email_service
        self.notification_service = notification_service

    def create_user(self, username: str, email: str) -> None:
        user_data = {"username": username, "email": email}
        self.database.save_user(user_data)
        self.email_service.send_welcome_email(email)
        self.notification_service.notify_user_created(username)


# 测试 DIP
def test_dip():
    print("=== 依赖反转原则示例 ===")

    # 使用不同的数据库实现
    postgres_db = PostgreSQLDatabase()
    memory_db = InMemoryDatabase()

    service1 = UserService(postgres_db)
    service1.create_user("alice", "alice@example.com")

    service2 = UserService(memory_db)
    service2.create_user("bob", "bob@example.com")

    # 使用依赖注入容器
    container = DependencyContainer()
    container.register(Database, PostgreSQLDatabase)
    container.register(EmailService, SMTPEmailService)

    database = container.resolve(Database)
    email_service = container.resolve(EmailService)

    print("\n=== 依赖注入示例 ===")

    # 在实际框架中，这部分通常由 DI 容器自动处理
    class ConsoleNotificationService:
        def notify_user_created(self, username: str) -> None:
            print(f"控制台通知: 用户 {username} 已创建")

    advanced_service = AdvancedUserService(
        database=database,
        email_service=email_service,
        notification_service=ConsoleNotificationService(),
    )
    advanced_service.create_user("charlie", "charlie@example.com")


test_dip()

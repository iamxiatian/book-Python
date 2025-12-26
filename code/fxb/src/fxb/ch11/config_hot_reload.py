import time
from threading import Lock
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, MySQLDsn

MY_ENV_DIR = Path(".") # 监控的环境变量所在目录
MY_ENV_FILES = [
    (MY_ENV_DIR / ".env.pydantic").resolve(strict=False),
    (MY_ENV_DIR / ".env.private").resolve(strict=False),
]

class DatabaseSettings(BaseSettings):
    url: MySQLDsn = Field(...)
    timeout: int = Field(30, ge=1)

class AppSettings(BaseSettings):
    database: DatabaseSettings
    debug: bool = Field(False)
    host: str = Field("0.0.0.0")
    port: int = Field(8000, ge=1, le=65535)

    model_config = SettingsConfigDict(
        env_prefix="MYAPP_",
        env_file=MY_ENV_FILES,
        env_file_encoding="utf-8",
        case_sensitive=False,
        env_nested_delimiter="__",
        extra="ignore",
    )


class ConfigManager:
    """配置管理器，支持热重载"""

    def __init__(self):
        self._settings = None
        self._lock = Lock() # 线程安全锁
        self._load_config()

        # 设置文件监视
        self.observer = Observer()
        event_handler = ConfigFileHandler(self)
        self.observer.schedule(event_handler, path=MY_ENV_DIR)
        self.observer.start()

    def _load_config(self):
        """加载或重新加载配置"""
        with self._lock:
            try:
                self._settings = AppSettings()
                print("配置重新加载成功")
            except Exception as e:
                print(f"配置加载失败: {e}")

    @property
    def settings(self) -> AppSettings:
        """获取当前配置（线程安全）"""
        with self._lock:
            return self._settings

    def stop(self):
        """停止文件监视"""
        self.observer.stop()
        self.observer.join()


class ConfigFileHandler(FileSystemEventHandler):
    """配置文件变更处理器"""

    def __init__(self, config_manager: ConfigManager):
        self.config_manager = config_manager

    def on_modified(self, event):
        if Path(event.src_path).resolve(strict=False) in MY_ENV_FILES:
            print(f"检测到配置文件变更: {event.src_path}")
            self.config_manager._load_config()
            # 输出最新配置
            settings = self.config_manager.settings
            print(f"[热重载] 端口: {settings.port}, 调试模式: {settings.debug}")


if __name__ == "__main__":
    manager = ConfigManager()

    try:
        # 模拟应用运行，每5秒打印当前配置
        while True:
            s = manager.settings
            print(f"端口: {s.port}, 超时: {s.database.timeout}, 调试: {s.debug}")
            time.sleep(5)
    except KeyboardInterrupt:
        manager.stop()
        print("配置管理器已停止")

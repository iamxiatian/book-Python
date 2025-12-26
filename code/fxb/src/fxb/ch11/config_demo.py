import json
import os
from dataclasses import dataclass
from typing import Optional

import tomllib
import yaml


@dataclass
class DbConf:
    """数据库配置组"""

    url: str
    timeout: int = 30

    @classmethod
    def from_dict(cls, data: dict) -> "DbConf":
        """从字典创建配置"""
        timeout = data.get("timeout", 30)
        return cls(url=data["url"], timeout=timeout)


@dataclass
class LogConf:
    """日志配置组"""

    level: str = "INFO"
    format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    file_path: Optional[str] = None
    max_size_mb: int = 100
    backup_count: int = 5

    @classmethod
    def from_dict(cls, data: dict) -> "LogConf":
        """从字典创建配置"""
        return cls(
            level=data.get("level", "INFO"),
            format=data.get("format", cls.format),
            file_path=data.get("file_path"),
            max_size_mb=data.get("max_size_mb", 100),
            backup_count=data.get("backup_count", 5),
        )


@dataclass
class AppConf:
    """应用主配置"""

    database: DbConf
    logging: LogConf
    debug: bool = False
    host: str = "0.0.0.0"
    port: int = 8000

    @classmethod
    def from_json(cls, filepath: str) -> "AppConf":
        """从JSON文件加载配置"""
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        return  cls(
                database=DbConf.from_dict(data["database"]),
                logging=LogConf.from_dict(data.get("logging", {})),
                debug=data.get("debug", False),
                host=data.get("host", "0.0.0.0"),
                port=data.get("port", 8000),
            )

    @classmethod
    def from_yaml(cls, filepath: str) -> "AppConf":
        """从YAML文件加载配置"""
        with open(filepath, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        return cls(
            database=DbConf.from_dict(data["database"]),
            logging=LogConf.from_dict(data.get("logging", {})),
            debug=data.get("debug", False),
            host=data.get("host", "0.0.0.0"),
            port=data.get("port", 8000),
        )

    @classmethod
    def from_toml(cls, filepath: str) -> "AppConf":
        """从TOML文件加载配置"""
        with open(filepath, "rb") as f:
            data = tomllib.load(f)

        return cls(
            database=DbConf.from_dict(data["database"]),
            logging=LogConf.from_dict(data.get("logging", {})),
            debug=data.get("debug", False),
            host=data.get("host", "0.0.0.0"),
            port=data.get("port", 8000),
        )

    def validate(self):
        """验证配置的完整性和正确性"""
        if not self.database.url:
            raise ValueError("数据库URL不能为空")

        valid_log_levels = ["DEBUG", "INFO", "WARNING", "ERROR"]
        if self.logging.level not in valid_log_levels:
            raise ValueError(f"日志级别必须是: {valid_log_levels}")

        if self.port < 1 or self.port > 65535:
            raise ValueError(f"端口值{self.port}不在1-65535之间")


if __name__ == "__main__":
    # JSON格式示例
    folder = os.path.dirname(os.path.abspath(__file__))
    print(f"当前路径: {folder}")
    conf_json = AppConf.from_json(f"{folder}/config.json")
    conf_json.validate()
    print(f"\n[JSON]数据库URL: {conf_json.database.url}")
    print(f"[JSON]日志级别: {conf_json.logging.level}")
    print(f"应用运行在: {conf_json.host}:{conf_json.port}")

    conf_yaml = AppConf.from_yaml(f"{folder}/config.yaml")
    conf_yaml.validate()
    print(f"[YAML]数据库URL: {conf_yaml.database.url}")
    print(f"[YAML]日志级别: {conf_yaml.logging.level}")

    # TOML格式示例
    conf_toml = AppConf.from_toml(f"{folder}/config.toml")
    conf_toml.validate()
    print(f"\n[TOML]数据库URL: {conf_toml.database.url}")
    print(f"[TOML]日志级别: {conf_toml.logging.level}")

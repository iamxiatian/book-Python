import os
import sys
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv


class EnvironmentManager:
    """环境配置管理器"""

    def __init__(self, app_env: Optional[str] = None):
        # 获取当前环境的类型（如：development, production, testings）
        self.app_env = app_env or os.getenv("APP_ENV", "development")
        self.project_root = Path.cwd()

    def setup_environment(self) -> bool:
        """设置环境配置，返回是否成功"""

        # 按优先级加载配置文件
        config_files = [
            ".env",  # 基础配置
            f".env.{self.app_env}",  # 环境特定配置
            ".env.local",  # 本地覆盖配置
        ]

        loaded_files = []
        for config_file in config_files:
            file_path = self.project_root / config_file
            if file_path.exists():
                load_dotenv(file_path, override=True)
                loaded_files.append(config_file)

        if not loaded_files:
            print("未找到任何配置文件")
            return False

        # 验证必需配置
        required_vars = ["DATABASE_URL", "XX_API_KEY"]
        missing_required = []

        for var in required_vars:
            if os.getenv(var) is None:
                missing_required.append(var)

        if missing_required:
            print("缺失必需的环境变量:")
            for var in missing_required:
                print(f"   - {var}")
            return False

        return True

    def get_value(self, key: str, default: Optional[str] = None):
        """获取配置值，支持类型转换"""
        value = os.getenv(key, default)

        if value is None:
            return None

        # 布尔值转换
        if value.lower() in ("true", "1", "yes", "y", "on"):
            return True
        elif value.lower() in ("false", "0", "no", "n", "off"):
            return False

        # 数值转换
        if value.isdigit():
            return int(value)

        # 列表转换（逗号分隔）
        if "," in value:
            return [item.strip() for item in value.split(",")]

        return value


def main():
    """主函数：配置环境并启动应用"""
    env_manager = EnvironmentManager()

    if not env_manager.setup_environment():
        print("环境配置失败，应用无法启动")
        sys.exit(1)

    # 获取配置值
    debug_mode = env_manager.get_value("DEBUG_MODE", "False")
    db_url = env_manager.get_value("DATABASE_URL")
    print("环境配置完成，应用准备启动")
    print(f"调试模式: {debug_mode}")
    print(f"数据库URL: {db_url}")

    # 这里可以继续启动应用逻辑
    return True


if __name__ == "__main__":
    main()

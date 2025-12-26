from dotenv import load_dotenv
import os

# 基础加载：自动查找当前目录或父目录中的.env文件
load_dotenv()

# 或指定具体文件路径
load_dotenv(".env.development", override=True)

# 访问配置值
database_url = os.getenv("DATABASE_URL")
api_key = os.getenv("XX_API_KEY")
debug_mode = os.getenv("DEBUG_MODE", "False").lower() == "true"
max_workers = int(os.getenv("MAX_WORKERS", "4"))
print(f"Database URL: {database_url}")
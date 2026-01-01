from loguru import logger
import sys

# 1. 移除默认配置，添加自定义配置
logger.remove()  # 移除所有已有处理器

# 2. 添加控制台处理器（带颜色）
logger.add(sys.stderr, level="INFO", colorize=True)

# 3. 添加文件处理器（按大小轮转）
logger.add(
    "app.log",
    rotation="10 MB",  # 文件达到10MB时轮转
    retention="7 days",  # 保留7天的日志
    compression="zip",  # 轮转后压缩
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    level="DEBUG",
    encoding="utf-8",
)

# 4. 使用示例
logger.debug("这是一条调试信息")
logger.info("这是一条普通信息", extra_info="附加数据")
logger.warning("这是一条警告信息")

try:
    1 / 0
except ZeroDivisionError as e:
    logger.error("发生除零错误", exc_info=e)

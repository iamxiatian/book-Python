import os
import structlog
from fxb.ch12.env_aware_logging import setup_env_aware_logging

if __name__ == "__main__":
    # 设置环境变量（在实际项目中通过外部配置）
    os.environ["APP_MODE"] = "dev"  # 或者：test, production

    # 初始化日志配置
    setup_env_aware_logging()
    logger = structlog.get_logger(__name__)
    # 测试不同级别的日志
    logger.debug("Debug text", extra={"extra_key": "extra_value"})
    logger.info("Info text")
    logger.warning("Warning text", ip="192.168.1.100")

    try:
        1 / 0  # 故意引发除零错误
    except ZeroDivisionError as e:
        logger.error("Error text", exc_info=True, msg=str(e))

import logging
from logging.handlers import TimedRotatingFileHandler


def setup_logging() -> None:
    """
    配置root logger，尽早调用一次即可。多次调用结果相同，避免重复添加处理器。
    """
    root = logging.getLogger()
    if root.hasHandlers():
        return  # 若已配过handler，直接返回，避免重复

    # 1. 全局最低级别（下游logger可以设得更细）
    root.setLevel(logging.DEBUG)

    # 2. 控制台handler：INFO及以上级别
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # 3. 按天切文件handler：DEBUG及以上级别，保留7天
    file_handler = TimedRotatingFileHandler(
        filename="app.log",
        when="midnight",  # 每天午夜轮转
        interval=1,  # 间隔1天
        backupCount=7,  # 保留7个备份文件
        encoding="utf-8",
    )
    file_handler.setLevel(logging.DEBUG)

    # 4. 设置日志格式
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)-8s] %(name)s:%(filename)s:%(lineno)d - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # 5. 全部挂到 root logger
    root.addHandler(console_handler)
    root.addHandler(file_handler)


if __name__ == "__main__":
    # 最早、只一次地调用配置函数
    setup_logging()

    # 任意模块里通过__name__获取logger
    logger = logging.getLogger(__name__)  # 名字为 __main__
    logger.debug("debug -> 只写文件")  # DEBUG级别：仅文件记录
    logger.info("info -> 文件+控制台")  # INFO级别：文件和控制台都记录
    logger.warning("warning -> 文件+控制台")  # WARNING级别：文件和控制台都记录

    try:
        1 / 0
    except ZeroDivisionError:
        # exc_info=True会记录完整的异常堆栈
        logger.error("发生除零错误", exc_info=True)

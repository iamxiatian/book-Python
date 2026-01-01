import structlog
import logging
from logging.handlers import TimedRotatingFileHandler


def setup_logging_with_structlog():
    """
    配置 structlog + 标准logging 实现结构化日志和文件轮转
    主要实现以下功能：
    1. 控制台输出（INFO级别以上，带颜色）
    2. 文件输出（DEBUG级别以上，按天轮转，保留7天，以json格式输出）
    """

    # 1. 配置标准 logging 作为底层日志框架
    # 获取根日志记录器，设置最低日志级别为DEBUG（确保所有日志都能被捕获）
    root_logger = logging.getLogger()
    if root_logger.hasHandlers():
        return  # 若已配过handler，直接返回，避免重复

    root_logger.setLevel(logging.DEBUG)

    # 创建控制台处理器 - 输出到标准输出，只记录INFO及以上级别
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # 创建文件轮转处理器 - 按天轮转日志文件，保留最近7天的日志
    file_handler = TimedRotatingFileHandler(
        filename="app.log",
        when="midnight",  # 每天午夜轮转
        interval=1,  # 间隔1天
        backupCount=7,  # 保留7个备份文件
        encoding="utf-8",
    )
    file_handler.setLevel(logging.DEBUG)  # 文件记录更详细的DEBUG级别日志

    # 2. 配置structlog使用标准logging作为后端
    # processors定义了日志事件的处理管道，每个处理器按顺序执行
    structlog.configure(
        processors=[
            # 根据日志级别过滤事件
            structlog.stdlib.filter_by_level,
            # 添加日志记录器名称
            structlog.stdlib.add_logger_name,
            # 添加日志级别
            structlog.stdlib.add_log_level,
            # 格式化位置参数
            structlog.stdlib.PositionalArgumentsFormatter(),
            # 添加时间戳，使用自定义格式
            structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S"),
            # 添加堆栈信息（当记录异常时）
            structlog.processors.StackInfoRenderer(),
            # 格式化异常信息
            structlog.processors.format_exc_info,
            # 将处理结果包装成适合标准logging处理器处理的格式
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        context_class=dict,  # 使用字典存储上下文信息
        logger_factory=structlog.stdlib.LoggerFactory(),  # logging作为日志工厂
        wrapper_class=structlog.stdlib.BoundLogger,  # 支持上下文绑定的记录器
        cache_logger_on_first_use=True,  # 缓存日志记录器以提高性能
    )

    # 3. 为控制台创建格式化器（使用彩色渲染）
    # ProcessorFormatter将标准logging的记录转换为structlog格式
    console_formatter = structlog.stdlib.ProcessorFormatter(
        # 控制台处理器使用彩色控制台渲染器
        processor=structlog.dev.ConsoleRenderer(colors=True),
        # 为通过标准logging直接记录的消息定义预处理链
        foreign_pre_chain=[
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S"),
        ],
    )
    console_handler.setFormatter(console_formatter)

    # 4. 为文件创建格式化器（使用JSON格式，便于日志分析）
    file_formatter = structlog.stdlib.ProcessorFormatter(
        # 文件处理器使用JSON渲染器，便于后续解析
        processor=structlog.processors.JSONRenderer(),
        # 同样为直接记录的消息定义预处理链
        foreign_pre_chain=[
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S"),
        ],
    )
    file_handler.setFormatter(file_formatter)

    # 5. 将处理器添加到根日志记录器
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)


if __name__ == "__main__":
    # 1. 初始化日志配置
    setup_logging_with_structlog()

    # 2. 获取 structlog 日志记录器
    # 使用 __name__ 作为记录器名称，这通常是模块的完整路径
    logger = structlog.get_logger(__name__)

    # 3. 演示 structlog 的各种特性

    # 特点1：结构化数据 - 可以随意添加字段
    logger.debug("debug -> 只写文件", extra_info="这是调试信息")
    logger.info("info -> 写入文件与控制台", user="小白", action="login")
    logger.warning("warning -> 写入文件与控制台", ip="192.168.1.100")

    # 特点2：上下文绑定 - 后续所有日志自动包含绑定的上下文信息
    # bind方法返回新的日志记录器，包含额外的上下文字段
    logger = logger.bind(req_id="1", endpoint="/api/user")
    logger.info("处理请求开始", method="GET")

    # 模拟异常操作
    try:
        1 / 0  # 故意引发除零错误
    except ZeroDivisionError as e:
        # 结构化异常记录 - exc_info=True会自动包含完整的异常信息
        logger.error("发生除零错误", exc_info=True, msg=str(e))

    logger.info("请求处理结束", status="failed", duration_ms=45.2)

    # 特点3：不同环境不同输出格式
    # - 控制台：人类可读的彩色输出（开发环境）
    # - 文件：机器可读的JSON格式（生产环境）
    # 在终端中运行会看到彩色输出，在文件中会是JSON格式

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, MySQLDsn
import os


class DatabaseSettings(BaseSettings):
    """
    数据库子配置组（嵌套配置）
    负责解析数据库相关的环境变量，封装数据库连接配置
    """

    # 核心字段：MySQL数据库连接URL（必填项，使用MySQLDsn类型自动校验URL格式）
    # ... 表示该字段为必填项，无默认值，必须从环境变量或者.env文件中读取
    url: MySQLDsn = Field(
        ...,
        description="MySQL数据库连接URL，例如：mysql://user:pass@localhost:3306/mydb",
    )
    # 连接超时时间：默认30秒，ge=1表示值必须大于等于1（避免无效的超时配置）
    timeout: int = Field(
        30, ge=1, description="数据库连接超时时间(秒)，最小值为1秒"
    )

    # 子配置的解析规则（此处不设置env_prefix，则交由外层AppSettings统一管理）
    model_config = SettingsConfigDict(
        # 关闭大小写敏感：环境变量DATABASE__URL和database__url会被视为同一个
        case_sensitive=False,
        # 忽略.env文件中未在当前类定义的配置项（避免因无关配置导致解析报错）
        extra="ignore",
    )


class AppSettings(BaseSettings):
    """
    应用主配置类（核心配置入口）
    整合所有子配置，统一读取.env文件并解析环境变量
    """

    # 嵌套配置：数据库子配置（由外层自动解析.env中的DATABASE__前缀变量初始化）
    # 仅声明类型，不手动初始化——Pydantic会通过env_nested_delimiter自动解析嵌套配置
    database: DatabaseSettings

    # 应用调试模式：默认关闭，可通过.env中的DEBUG变量覆盖
    debug: bool = Field(
        False, description="应用调试模式开关"
    )
    # 应用监听主机：默认0.0.0.0（监听所有网卡），适配多环境部署
    host: str = Field("0.0.0.0", description="监听主机地址")
    # 应用监听端口：默认8000，通过ge和lt参数限定范围1-65535（符合TCP端口规范）
    port: int = Field(8000, ge=1, le=65535, description="监听端口号")

    # 主配置的核心解析规则（决定.env文件如何被读取和解析）
    model_config = SettingsConfigDict(
        # 环境变量前缀：所有配置项的名称都会自动添加MYAPP_前缀，如MYAPP_DEBUG
        env_prefix="MYAPP_",
        # 指定.env文件路径，此处读取工作目录下的.env.pydantic和".env.pydantic2"
        env_file=(".env.pydantic", ".env.private"),
        # 配置文件编码：固定为utf-8，避免中文/特殊字符乱码
        env_file_encoding="utf-8",
        # 环境变量大小写不敏感：DEBUG和debug视为同一个变量
        case_sensitive=False,
        # 嵌套配置分隔符：DATABASE__URL会被解析为database.url（对应DatabaseSettings的url字段）， 这是嵌套配置能自动解析的核心配置！
        env_nested_delimiter="__",
        # 忽略.env中未定义在配置类中的变量（如日志级别、API密钥等无关配置）
        extra="ignore",
    )


# 安全加载配置（添加异常捕获，避免配置错误导致程序直接崩溃）
if __name__ == "__main__":
    try:
        # 初始化主配置实例（自动读取.env.pydantic并解析所有配置）
        settings = AppSettings()

        # 打印配置信息（验证解析结果）
        print("===== 应用配置加载成功 =====")
        print(f"数据库连接URL: {settings.database.url}")
        print(f"数据库连接超时: {settings.database.timeout} 秒")
        print(f"应用调试模式: {'开启' if settings.debug else '关闭'}")
        print(f"应用运行地址: http://{settings.host}:{settings.port}")

    except Exception as e:
        # 配置加载失败时，输出清晰的错误信息和调试线索
        print("===== 应用配置加载失败 =====")
        print(f"配置文件路径: {os.path.abspath(".env.pydantic")}")
        print(f"错误原因: {e}")

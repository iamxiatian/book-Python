"""
OpenTelemetry分布式追踪示例，同时输出追踪数据到控制台和Jaeger后端
"""

from opentelemetry import trace 
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider  
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,  # 批量处理器（提升性能）
    ConsoleSpanExporter,  # 控制台输出导出器（用于调试）
)

# 1. 配置服务资源信息
resource = Resource.create(
    {
        SERVICE_NAME: "order-service",  # 服务名称
        "deployment.environment": "production",  # 环境标识
    }
)

# 设置全局追踪提供者
trace.set_tracer_provider(TracerProvider(resource=resource))

# 2. 配置导出器
# 控制台导出器：开发环境调试使用
console_exporter = ConsoleSpanExporter()

# Jaeger导出器：生产环境使用，需确保Jaeger服务已启动
jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",  # Jaeger Agent地址
    agent_port=6831,  # Jaeger Agent端口
)

# 3. 注册处理器（支持多路输出）
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(console_exporter)  # 输出到控制台
)
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(jaeger_exporter)  # 输出到Jaeger
)

# 4. 获取Tracer实例
tracer = trace.get_tracer(__name__)

def process_order(order_id: str) -> str:
    """模拟订单处理流程，展示跨函数追踪"""

    # 创建并启动一个新的Span，命名为"process_order"
    with tracer.start_as_current_span("process_order") as span:
        # 为Span添加自定义属性，会在追踪后端（如Jaeger）中显示，便于查询和过滤
        span.set_attribute("order.id", order_id)  # 订单ID
        span.set_attribute("service.name", "order_service")  # 服务名称

        # ==================== 子操作1：验证 ====================
        # 创建子Span（自动建立父子关系），父子关系形成了调用链的层次结构
        with tracer.start_as_current_span("validate") as validate_span:
            # 放置实际的验证逻辑，如检查订单状态、验证用户权限等

            # 为验证Span添加相关属性
            validate_span.set_attribute("validation.status", "passed")

        # ==================== 子操作2：支付 ====================
        # 创建另一个子Span（与验证Span是兄弟关系，都是process_order的子节点）
        with tracer.start_as_current_span("payment") as payment_span:
            # 放置实际的支付逻辑，如调用支付网关、扣款等

            payment_span.set_attribute("payment.method", "credit_card")
            payment_span.set_attribute("payment.amount", "100.00")

        # 注意：所有Span会在with块结束时自动结束，并记录时间、状态等相关元数据
        return f"Order {order_id} processed"

if __name__ == "__main__":
    result = process_order("12345")
    print(result)

    print("\n说明：")
    print("- 控制台已输出追踪信息")
    print("- 如需查看Jaeger可视化界面：")
    print(
        "  1. 启动Jaeger: docker run -d -p 16686:16686 jaegertracing/all-in-one"
    )
    print("  2. 访问: http://localhost:16686")

"""
FastAPI应用集成Prometheus指标监控示例
该应用定义三种Prometheus指标类型，并通过/metrics端点暴露指标数据
"""

from prometheus_client import Counter, Gauge, Histogram, generate_latest
from fastapi import FastAPI, Response
import random
import time
import asyncio

# 初始化FastAPI应用
app = FastAPI()

# ==================== Prometheus指标定义 ====================
# 注意：指标定义应在应用启动时完成，确保全局唯一

# Counter类型：只增不减的计数器，适用于记录累计数量
# 参数说明：
#   1. "http_requests_total" - 指标名称，在Prometheus中查询时使用
#   2. "HTTP请求总数" - 指标描述，帮助理解指标含义
#   3. ["endpoint"] - 标签列表，用于维度划分，这里按接口端点分类
# 定义Prometheus指标
REQUEST_COUNT = Counter("http_requests_total", "HTTP请求总数", ["endpoint"])

# Histogram类型：直方图，适用于记录数值分布（如请求延迟）
# 参数说明：
#   1. "http_request_duration_seconds" - 指标名称
#   2. "请求处理时间" - 指标描述
REQUEST_DURATION = Histogram("http_request_duration_seconds", "请求处理时间")

# Gauge类型：仪表盘，适用于记录可增减的瞬时值
# 参数说明：
#   1. "active_sessions" - 指标名称
#   2. "当前活跃会话数" - 指标描述
ACTIVE_SESSIONS = Gauge("active_sessions", "当前活跃会话数")


@app.get("/api/data")
async def get_data():
    """模拟业务接口，每次请求都会更新指标，展示如何在实际业务中集成指标记录"""
    start_time = time.time()

    # 模拟异步处理逻辑
    await asyncio.sleep(random.uniform(0.01, 0.1))

    # ========== 更新Prometheus指标 ==========
    # 1. 更新请求计数器：为"/api/data"端点的计数器加1
    #    .labels()方法使用标签区分不同端点的请求
    REQUEST_COUNT.labels(endpoint="/api/data").inc()

    # 2. 记录请求处理耗时：将本次请求的处理时间记录到直方图中
    #    .observe()方法会自动将值分配到对应的bucket中
    REQUEST_DURATION.observe(time.time() - start_time)

    # 3. 更新活跃会话数：随机设置一个模拟值
    #    .set()方法直接设置仪表盘的当前值
    #    在实际应用中，这里可能是从共享状态或数据库中获取的真实值
    ACTIVE_SESSIONS.set(random.randint(10, 100))  # 设置活跃会话数

    return {"status": "ok", "data": "sample"}


@app.get("/metrics")
async def metrics():
    """
    暴露指标端点，Prometheus将定期访问此端点抓取指标数据
    这是Python应用与Prometheus监控系统集成的关键
    """
    # generate_latest()：生成Prometheus格式的指标数据
    #   该函数会将所有已注册的指标转换为Prometheus可识别的文本格式
    # Response：返回HTTP响应，指定内容类型为纯文本
    return Response(content=generate_latest(), media_type="text/plain")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000)

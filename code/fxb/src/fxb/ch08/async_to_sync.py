import asyncio
import time


def synchronous_blocking_function(duration: float) -> str:
    """模拟耗时的同步函数"""
    time.sleep(duration)
    return f"同步函数完成，耗时 {duration} 秒"


async def main():
    # 错误方式：直接调用会阻塞事件循环
    # result = synchronous_blocking_function(1.0)

    # 正确方式：使用 to_thread 在单独线程中执行
    result = await asyncio.to_thread(synchronous_blocking_function, 1.0)
    print(f"结果: {result}")

    # 并发执行多个同步函数
    tasks = [
        asyncio.to_thread(synchronous_blocking_function, 1.5),
        asyncio.to_thread(synchronous_blocking_function, 1.0),
        asyncio.to_thread(synchronous_blocking_function, 0.5),
    ]

    results = await asyncio.gather(*tasks)
    for r in results:
        print(f"并发结果: {r}")


if __name__ == "__main__":
    asyncio.run(main())

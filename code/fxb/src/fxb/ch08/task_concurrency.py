import asyncio
import time


async def say_after(delay: float, message: str):
    await asyncio.sleep(delay)
    print(message)
    return delay


async def sequential_execution():
    """顺序执行"""
    start_time = time.time()
    r1 = await say_after(1.0, "第一个消息")
    r2 = await say_after(1.0, "第二个消息")
    print(f"顺序执行结果: {r1}, {r2}, 耗时: {time.time() - start_time:.2f} 秒")


async def concurrent_execution():
    """并发执行"""
    start_time = time.time()
    task1 = asyncio.create_task(say_after(1.0, "第一个消息"))
    task2 = asyncio.create_task(say_after(1.0, "第二个消息"))

    r1 = await task1
    r2 = await task2
    print(f"并发执行结果: {r1}, {r2}, 耗时: {time.time() - start_time:.2f} 秒")


async def main():
    await sequential_execution()
    print()
    await concurrent_execution()


if __name__ == "__main__":
    asyncio.run(main())

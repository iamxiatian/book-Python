import asyncio


async def async_function(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"{name} 完成，等待 {delay} 秒"


# 方法1：使用 asyncio.run()（推荐）
def sync_caller_1():
    print("同步代码调用异步函数...")
    result = asyncio.run(async_function("任务A", 1.0))
    print(f"结果: {result}")


# 方法2：手动管理事件循环（不推荐）
def sync_caller_2():
    print("手动管理事件循环...")
    loop = asyncio.new_event_loop()

    try:
        result = loop.run_until_complete(async_function("任务B", 0.5))
        print(f"结果: {result}")
    finally:
        loop.close()


if __name__ == "__main__":
    sync_caller_1()
    print()
    sync_caller_2()

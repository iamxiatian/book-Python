import asyncio


async def slow_operation(delay: float):
    await asyncio.sleep(delay)
    return f"操作完成，耗时 {delay} 秒"


async def main():
    try:
        # 设置超时为 1.5 秒
        result = await asyncio.wait_for(slow_operation(2.0), timeout=1.5)
        print(f"成功: {result}(delay=2.0)")
    except asyncio.TimeoutError:
        print("操作超时！(delay=2.0)")

    # 成功的情况
    try:
        result = await asyncio.wait_for(slow_operation(1.0), timeout=1.5)
        print(f"成功: {result}(delay=1.0)")
    except asyncio.TimeoutError:
        print("操作超时！(delay=1.0)")


if __name__ == "__main__":
    asyncio.run(main())

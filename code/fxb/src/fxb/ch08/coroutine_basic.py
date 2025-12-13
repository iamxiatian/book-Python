import asyncio

async def simple_coroutine(name: str, delay: float) -> float:
    """简单的协程示例"""
    print(f"[{name}] 开始执行，等待 {delay} 秒")
    await asyncio.sleep(delay)  # 模拟异步 I/O 操作
    print(f"[{name}] 执行完成")
    return delay*10

async def demonstrate_coroutines():
    """演示协程的基本行为"""
    coro1 = simple_coroutine("协程1", 2.0) #\label{code:coroutine:basic:1}#
    coro2 = simple_coroutine("协程2", 1.0)

    print(f"coro1 类型: {type(coro1)}")

    # 使用 await 顺序执行协程
    result1 = await coro1
    result2 = await coro2
    print(f"结果: {result1}, {result2}")

if __name__ == "__main__":
    asyncio.run(demonstrate_coroutines())
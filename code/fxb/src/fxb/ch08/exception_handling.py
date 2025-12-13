from typing import NoReturn
import asyncio


async def task_with_result(name: str, result: str)->str:
    return f"{name}: {result}"


async def task_with_exception(name: str)->NoReturn:
    raise ValueError(f"{name} 抛出了异常")


async def main():
    tasks = [
        task_with_result("A", "成功"),
        task_with_exception("B"),
        task_with_result("C", "成功"),
    ]

    # 默认行为：遇到异常立即抛出，此时得不到results信息
    try:
        results = await asyncio.gather(*tasks)
    except ValueError as e:
        print(f"默认模式捕获到异常: {e}")

    # 返回异常模式，任务需重新实例化，否则提示：cannot reuse already awaited coroutine
    tasks = [
        task_with_result("A", "成功"),
        task_with_exception("B"),
        task_with_result("C", "成功"),
    ]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    print("\n使用 return_exceptions=True 的结果:")
    for i, r in enumerate(results):
        if isinstance(r, Exception):
            print(f"任务 {i}: 异常 - {r}")
        else:
            print(f"任务 {i}: 成功 - {r}")


if __name__ == "__main__":
    asyncio.run(main())

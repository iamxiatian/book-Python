import asyncio


async def long_running_task(name: str, seconds: int)->str:
    print(f"任务 {name} 开始，需要 {seconds} 秒")
    await asyncio.sleep(seconds)
    print(f"任务 {name} 完成")
    return f"{name}:{seconds}"


async def main():
    # 创建任务
    task_a = asyncio.create_task(long_running_task("A", 3))
    task_b = asyncio.create_task(long_running_task("B", 2))
    task_c = asyncio.create_task(long_running_task("C", 1))

    print("所有任务已创建，开始并发执行...")

    # 等待所有任务完成，并收集结果
    results = await asyncio.gather(task_a, task_b, task_c)
    # results = await asyncio.gather(
    #     long_running_task("A", 3),
    #     long_running_task("B", 2),
    #     long_running_task("C", 1),
    # )
    print(f"所有任务完成，结果: {results}")


if __name__ == "__main__":
    asyncio.run(main())

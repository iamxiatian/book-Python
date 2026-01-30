import asyncio


async def worker(name: str, delay: float)->str:
    print(f"{name} 开始工作")
    await asyncio.sleep(delay)
    if name == "B" and delay > 1:
        raise ValueError(f"{name} 出错了!")
    print(f"{name} 工作完成")
    return f"{name} 结果"


async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            # 创建任务组内的任务
            t1 = tg.create_task(worker("A", 3.5))
            t2 = tg.create_task(worker("B", 2.5))  # 这个会出错, 改成0.5则正常
            t3 = tg.create_task(worker("C", 0.5))

        # 如果所有任务成功完成，继续执行
        print(f"所有任务成功: {t1.result()}, {t2.result()}, {t3.result()}")
    except* ValueError as eg:
        # 处理部分任务失败的情况
        for exc in eg.exceptions:
            print(f"任务出错: {exc}")


if __name__ == "__main__":
    asyncio.run(main())

import asyncio


async def cancellable_task():
    try:
        print("任务开始")
        await asyncio.sleep(5)  # 模拟长时间运行
        print("任务正常完成")
        return "结果"
    except asyncio.CancelledError:
        print("任务被取消，正在清理资源...")
        raise  # 重新抛出异常是标准做法


async def main():
    task = asyncio.create_task(cancellable_task())

    # 等待1秒后取消任务,此时任务还没有结束，因此会抛出异常
    await asyncio.sleep(1)
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("主函数中捕获到取消异常")


if __name__ == "__main__":
    asyncio.run(main())

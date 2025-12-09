import multiprocessing
import time
import os


def cpu_intensive_task(n):
    """模拟CPU密集型任务：计算斐波那契数列"""
    pid = os.getpid()
    print(f"进程 {pid} 开始执行任务")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    print(f"进程 {pid} 完成任务")
    return a


def basic_multiprocessing():
    n = 500_000  # 一个较大的数字，模拟计算密集型任务
    processes = []
    start = time.time()

    # 1. 创建4个进程并行执行任务
    for i in range(4):
        p = multiprocessing.Process(target=cpu_intensive_task, args=(n,))
        p.start()
        processes.append(p)

    # 等待所有进程完成
    for p in processes:
        p.join()

    print(f"多进程总耗时: {time.time() - start:.2f}秒")

    # 2. 要求顺序执行4次CPU密集型任务
    start = time.time()
    for _ in range(4):
        cpu_intensive_task(n)
    print(f"顺序执行耗时: {time.time() - start:.2f}秒")

if __name__ == "__main__":
    basic_multiprocessing()

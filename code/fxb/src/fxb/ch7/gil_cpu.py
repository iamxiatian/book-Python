import threading
import time
import os
import sys


def cpu_task(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b


def test_cpu():
    n = 500_000  # 一个较大的数字，模拟计算密集型任务
    print(f"Python版本：{sys.version}")
    print(f"CPU 核心数（逻辑核）：{os.cpu_count()}")

    # 1. 要求四个线程并发执行CPU密集型任务
    threads = []
    start = time.time()
    for _ in range(4):
        t = threading.Thread(target=cpu_task, args=(n,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print(f"多线程耗时: {time.time() - start:.2f}秒")

    # 2. 要求顺序执行4次CPU密集型任务
    start = time.time()
    for _ in range(4):
        cpu_task(n)
    print(f"单线程耗时: {time.time() - start:.2f}秒")


if __name__ == "__main__":
    test_cpu()

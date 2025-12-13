import threading
import time


class SimpleCounter:
    """线程不安全的计数器"""

    def __init__(self):
        self.value = 0

    def increment(self):
        time.sleep(0.001)  # 模拟耗时操作，放大竞态条件
        self.value += 1


class SafeCounter:
    """线程安全的计数器"""

    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            time.sleep(0.001)  # 模拟耗时操作，放大竞态条件
            self.value += 1


def worker(counter, times):
    for _ in range(times):
        counter.increment()


def test_counter():
    simple_counter = SimpleCounter()
    threads = []
    for _ in range(10):
        t = threading.Thread(target=worker, args=(simple_counter, 1000))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print(f"最终计数(线程不安全): {simple_counter.value}")  # 不一定是10000

    safe_counter = SafeCounter()
    threads = []
    for _ in range(10):
        t = threading.Thread(target=worker, args=(safe_counter, 1000))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print(f"最终计数(线程安全): {safe_counter.value}")  # 应为 10000


if __name__ == "__main__":
    test_counter()
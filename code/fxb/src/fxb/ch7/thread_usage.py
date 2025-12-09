import threading
import time


# 方式一：直接使用Thread类, 后面使用target参数指定线程要执行该函数
def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(0.5)


# 方式二：继承 Thread 类
class WorkerThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f"{self.name} 开始执行")
        time.sleep(1)
        print(f"{self.name} 执行结束")


def demo_thread_creation():
    print("--- 方式一：直接实例化 Thread ---")
    thread1 = threading.Thread(target=print_numbers, name="数字打印线程")
    thread1.start()
    thread1.join()

    print("\n--- 方式二：继承 Thread 类 ---")
    thread2 = WorkerThread("工作线程")
    thread2.start()
    thread2.join()


if __name__ == "__main__":
    demo_thread_creation()

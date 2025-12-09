import multiprocessing
import time

def square(x):
    """计算平方（模拟CPU密集型任务）"""
    time.sleep(0.5)  # 模拟计算耗时
    return x * x

def demo_multiprocessing_pool():
    numbers = list(range(1, 11))
    
    print("=== 方法1: 同步map() ===")
    start = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(square, numbers)
    print(f"结果: {results}")
    print(f"耗时: {time.time() - start:.2f}秒")
    
    print("\n=== 方法2: 异步map_async() ===")
    start = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        async_result = pool.map_async(square, numbers)
        # 可以在这里执行其他任务
        results = async_result.get()  # 阻塞等待结果
    print(f"结果: {results}")
    print(f"耗时: {time.time() - start:.2f}秒")
    
    print("\n=== 方法3: imap_unordered()（按完成顺序）===")
    start = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        for result in pool.imap_unordered(square, numbers):
            print(f"{result}", end=", ")
    print(f"\n总耗时: {time.time() - start:.2f}秒")

if __name__ == "__main__":
    demo_multiprocessing_pool()
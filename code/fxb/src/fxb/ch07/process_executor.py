from concurrent.futures import ProcessPoolExecutor, as_completed
import time


def square(x):
    time.sleep(0.5)
    return x * x


def demo_process_pool_executor():
    numbers = list(range(1, 4))

    print("=== 使用 submit() 和 as_completed() ===")
    start = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(square, num): num for num in numbers}
        results = []
        for future in as_completed(futures):
            num = futures[future]
            result = future.result()
            results.append((num, result))
            print(f"数字 {num} 的平方为 {result}")

    # 按原顺序排序输出
    results.sort(key=lambda x: x[0])
    print(f"完整结果: {[r[1] for r in results]}")
    print(f"耗时: {time.time() - start:.2f}秒")

    print("\n=== 使用 map() ===")
    start = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(square, numbers))
    print(f"结果: {results}")
    print(f"耗时: {time.time() - start:.2f}秒")

if __name__ == "__main__":
    demo_process_pool_executor()

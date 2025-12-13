from concurrent.futures import ThreadPoolExecutor, as_completed, wait
import time
import random


def download_file(url) -> tuple[str, int]:
    """模拟下载文件"""
    print(f"开始下载: {url}")
    time.sleep(random.uniform(0.5, 2.0))  # 模拟下载时间
    size = random.randint(100, 1000)  # 模拟文件大小
    print(f"下载完成: {url}, 大小: {size}KB")
    return url, size


def demo_thread_pool():
    urls = [
        "https://example.com/file1.zip",
        "https://example.com/file2.zip",
        "https://example.com/file3.zip",
        "https://example.com/file4.zip",
        "https://example.com/file5.zip",
    ]

    with ThreadPoolExecutor(max_workers=3) as executor:
        print("=== 方法1: submit() 每次提交单个任务 ===")
        for url in urls:
            future = executor.submit(download_file, url)
            url, size = future.result()
            print(f"单个任务结果: {url} -> {size}KB")

    with ThreadPoolExecutor(max_workers=3) as executor:
        print("\n=== 方法2: map() 批量提交，按提交顺序获取结果 ===")
        for url, size in executor.map(download_file, urls):
            print(f"获取结果: {url} -> {size}KB")

    with ThreadPoolExecutor(max_workers=3) as executor:
        print(
            "\n=== 方法3: submit()批量提交，借助as_completed按完成顺序获取结果 ==="
        )
        futures = {executor.submit(download_file, url): url for url in urls}
        for future in as_completed(futures):
            url, size = future.result()
            print(f"先完成的任务: {url} -> {size}KB")


if __name__ == "__main__":
    demo_thread_pool()

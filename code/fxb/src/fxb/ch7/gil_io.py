import threading
import requests
import time


def fetch(url):
    resp = requests.get(url)
    return resp.status_code


def test_io():
    urls = ["https://httpbin.org/delay/1"] * 4
    threads = []
    start = time.time()
    for url in urls:
        t = threading.Thread(target=fetch, args=(url,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print(f"多线程耗时: {time.time() - start:.2f}秒")

    # 1. 要求顺序执行4次CPU密集型任务
    start = time.time()
    for url in urls:
        fetch(url)
    print(f"单线程耗时: {time.time() - start:.2f}秒")

if __name__ == "__main__":
    test_io()
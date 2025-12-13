import threading
import queue
import time

# 水果队列，最多存放5个水果
fruit_queue = queue.Queue(maxsize=5)


def farmer(farmer_id: int):
    """果农：生产水果放入队列"""
    fruits = ["苹果", "香蕉", "橙子", "葡萄", "西瓜"]
    for fruit in fruits:
        time.sleep(0.2)  # 模拟生产时间
        fruit_queue.put(f"果农{farmer_id}的{fruit}")
        print(f"果农{farmer_id}生产了: {fruit}")


def clerk(clerk_id: int):
    """店员：从队列取出水果销售"""
    while True:
        try:
            fruit = fruit_queue.get(timeout=3)  # 3秒超时
            time.sleep(0.3)  # 模拟销售时间
            print(f"店员{clerk_id}售出了: {fruit}")
            fruit_queue.task_done()  # 标记任务完成
        except queue.Empty:
            break


# 创建3个果农线程和2个店员线程
threads = [
    threading.Thread(target=farmer, args=(1,)),
    threading.Thread(target=farmer, args=(2,)),
    threading.Thread(target=farmer, args=(3,)),
    threading.Thread(target=clerk, args=(1,)),
    threading.Thread(target=clerk, args=(2,)),
]

for t in threads:
    t.start()

# 等待所有任务完成
fruit_queue.join()

for t in threads:
    t.join()

print("今日水果销售完毕！")

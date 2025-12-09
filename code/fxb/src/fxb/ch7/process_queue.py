import multiprocessing
import time
import random

# 存入水果的仓库：采用队列方式，最多存放5个水果
warehouse = multiprocessing.Queue(maxsize=5)


def farmer(queue: multiprocessing.Queue, farmer_id:int, fruit_types:list):
    """果农：生产水果放入队列"""
    for fruit in fruit_types:
        # 模拟批发准备时间
        time.sleep(random.uniform(0.1, 0.3))
        batch = f"果农{farmer_id}的{fruit}批次{random.randint(1, 100)}"
        queue.put(batch)
        print(f"{batch} 已放入仓库")

    # 放入结束标志
    queue.put("DONE")


def clerk(queue: multiprocessing.Queue, clerk_id: int):
    """店员：从队列取出水果销售"""
    count = 0
    while True:
        # 从仓库获取水果批次
        batch = queue.get()

        if batch == "DONE":
            # 重新放入队列，为其他零售商传递结束信号
            queue.put("DONE")
            break

        # 模拟零售准备时间
        time.sleep(random.uniform(0.2, 0.4))
        count += 1
        print(f"店员{clerk_id} 售出: {batch} (累计: {count}批)")


def demo_fruit_queue():
    # 创建水果仓库队列，最多容纳20个批次
    warehouse = multiprocessing.Queue(maxsize=20)

    # 水果种类
    fruit_varieties = ["苹果", "香蕉", "橙子", "葡萄", "西瓜"]

    # 创建2个果农进程和3个店员进程
    farmers = [
        multiprocessing.Process(
            target=farmer, args=(warehouse, i, fruit_varieties)
        )
        for i in range(1, 3)
    ]

    clerks = [
        multiprocessing.Process(target=clerk, args=(warehouse, i))
        for i in range(1, 4)
    ]

    # 启动所有进程
    for f in farmers:
        f.start()

    for c in clerks:
        c.start()

    for f in farmers:
        f.join()
    for c in clerks:
        c.join()
        
    print("今日水果销售完毕！")


if __name__ == "__main__":
    demo_fruit_queue()

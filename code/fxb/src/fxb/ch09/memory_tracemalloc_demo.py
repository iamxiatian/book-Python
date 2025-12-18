import tracemalloc
from .memory_leak_demo import DataItem, DataProcessor

def analyze_memory_allocation():
    """分析内存分配情况"""
    # 启动内存追踪，记录10帧的调用栈信息
    tracemalloc.start(10)

    # 拍摄第一个快照（基线）
    snapshot1 = tracemalloc.take_snapshot()

    # 执行代码
    processor = DataProcessor()
    for i in range(1000):
        item = DataItem(f"ANALYZE_{i}")
        processor.process_item(item)

    # 拍摄第二个快照
    snapshot2 = tracemalloc.take_snapshot()

    # 比较快照，按代码行统计
    stats = snapshot2.compare_to(snapshot1, "lineno")

    print("内存分配最多的3个位置:")
    for stat in stats[:3]:
        print(f"  {stat}")

    # 获取内存分配最多的位置的调用栈
    top_stats = snapshot2.compare_to(snapshot1, "traceback")
    if top_stats:
        top = top_stats[0]
        print("\n内存分配最多的调用栈:")
        print("\n".join(top.traceback.format()))

    tracemalloc.stop()


def find_memory_leak():
    """查找内存泄漏"""
    tracemalloc.start()

    # 创建两个快照，对比内存变化
    snapshot1 = tracemalloc.take_snapshot()

    # 执行可能泄漏内存的代码
    processor = DataProcessor()
    for i in range(10000):
        item = DataItem(f"LEAK_{i}")
        processor.process_item(item)

    snapshot2 = tracemalloc.take_snapshot()

    # 比较差异，找出内存增长最大的位置
    top_stats = snapshot2.compare_to(snapshot1, "lineno")

    print("内存增长最大的前3行代码:")
    for stat in top_stats[:3]:
        print(f"  {stat}")


if __name__ == "__main__":
    analyze_memory_allocation()
    input("hello")

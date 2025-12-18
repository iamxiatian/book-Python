import os


class DataItem:
    """数据项类，模拟占用内存的对象"""

    def __init__(self, item_id):
        self.item_id = item_id
        # 模拟占用较大内存的数据
        self.data = os.urandom(1024)  # 每个对象1KB数据

    def __del__(self):
        print(f"数据项 {self.item_id} 被销毁")


class DataProcessor:
    """数据处理类 - 存在内存泄漏"""

    processed_items = []  # 问题：全局缓存所有处理过的数据项

    def process_item(self, item):
        """处理数据项"""
        item.processed = True
        self.processed_items.append(item)  # 添加到全局列表
        return True


def demo_memory_leak():
    """演示内存泄漏"""
    processor = DataProcessor()

    # 处理多个数据项
    for i in range(100):
        item = DataItem(f"ITEM_{i}")
        processor.process_item(item)

    print(f"\n全局缓存大小: {len(DataProcessor.processed_items)}")
    # 问题：即使此后不再需要这些数据项，它们仍被全局列表引用，无法释放
    # 随着时间推移，缓存会不断增长，最终导致内存耗尽
    
if __name__ == "__main__":
    demo_memory_leak()
    print("\n内存泄漏演示结束")

from memory_profiler import profile
from .memory_leak_demo import DataProcessor, DataItem


@profile
def memory_intensive_operation():
    """内存密集型操作示例"""
    processor = DataProcessor()

    # 创建一个占用大量内存的列表
    large_list = [DataItem(f"LIST_{i}") for i in range(10000)]

    # 处理这些数据项
    for item in large_list:
        processor.process_item(item)

    return len(DataProcessor.processed_items)


if __name__ == "__main__":
    memory_intensive_operation()
    input("Press Enter to exit...")

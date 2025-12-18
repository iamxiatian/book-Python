import gc
from . memory_leak_demo import DataItem, DataProcessor

def check_objects_count():
    """检查对象数量变化"""
    before_count = len(gc.get_objects())
    print(f"初始对象数量: {before_count}")

    # 执行可能增加对象的代码
    processor = DataProcessor()
    for i in range(100):
        item = DataItem(f"TEST_{i}")
        processor.process_item(item)

    after_count = len(gc.get_objects())
    print(f"执行后对象数量: {after_count}")
    print(f"对象增加数量: {after_count - before_count}")

    # 查看最近创建的对象类型
    print("\n最近创建的5个对象类型:")
    for obj in gc.get_objects()[-5:]:
        print(f"  {type(obj).__name__}: {repr(obj)[:80]}...")


if __name__ == "__main__":
    check_objects_count()

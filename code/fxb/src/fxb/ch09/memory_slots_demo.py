import tracemalloc
import time


class DataItemWithDict:
    """使用默认__dict__的类"""

    def __init__(self, id: int, data: str):
        self.id = id
        self.data = data


class DataItemWithSlots:
    """使用__slots__的类"""

    __slots__ = ("id", "data")

    def __init__(self, id: int, data: str):
        self.id = id
        self.data = data


def measure(cls, n_objects=1_000_000):
    """测量类创建对象的内存使用和性能"""
    # 启动内存跟踪
    tracemalloc.start()

    # 创建对象
    start_time = time.time()
    items = [cls(i, "测试数据") for i in range(n_objects)]
    creation_time = time.time() - start_time

    # 测量内存
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # 测试属性访问速度
    start_time = time.time()
    for item in items:
        _ = item.id
        _ = item.data
    access_time = time.time() - start_time

    return {
        "内存占用(MB)": peak / 1024 / 1024,
        "对象创建时间(秒)": creation_time,
        "属性访问时间(秒)": access_time,
    }


def main():
    print("测试普通类（使用默认__dict__）:")
    results1 = measure(DataItemWithDict)
    for k, v in results1.items():
        print(f"  {k}: {v:.6f}")

    print("\n测试使用 __slots__ 的类:")
    results2 = measure(DataItemWithSlots)
    for k, v in results2.items():
        print(f"  {k}: {v:.6f}")

    # 计算差异百分比
    print("\n性能提升百分比:")
    for k in results1:
        improvement = (results1[k] - results2[k]) / results1[k] * 100
        print(f"  {k}: 提升 {improvement:.2f}%")

    # 普通对象可以动态添加属性，背后是一个字典
    print("\n动态属性添加演示:")
    normal_obj = DataItemWithDict(1, "示例数据")
    normal_obj.porcessed = True  #  # 可以正常添加新属性
    print(f"  普通对象属性字典: {normal_obj.__dict__}")
    # 以下测试报错，读者可自行测试
    # slots_obj = DataItemWithSlots(2, "示例数据")
    # slots_obj.processed = True  # 抛出AttributeError：has no attribute 'processed'
    # print(slots_obj.__dict__) # 抛出AttributeError：has no attribute '__dict__'


if __name__ == "__main__":
    main()

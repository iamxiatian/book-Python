import tracemalloc
import time


class ParentClass:
    """使用默认__dict__的类"""
    __slots__ = ("id", "data")
    def __init__(self, id: int, data: str):
        self.id = id
        self.data = data


class ChildClass(ParentClass):
    def __init__(self, id: int, data: str):
        self.id = id
        self.data = data


class ChildClass2(ParentClass):
    __slots__ = ("processed",)
    
    def __init__(self, id: int, data: str):
        self.id = id
        self.data = data


def main():
    child = ChildClass(1, "测试数据")
    child.processed = True
    print(child.__dict__)

    child = ChildClass2(1, "测试数据")
    child.processed = True
    #print(child.__dict__)


if __name__ == "__main__":
    main()

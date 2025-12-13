class SingletonByNew:
    """基于 __new__ 方法的单例模式"""

    _instance = None  # 类变量，用于存储唯一实例

    def __new__(cls, *args, **kwargs):
        # 如果实例不存在，则创建新实例
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("创建单例实例")
        return cls._instance

    def __init__(self):
        # 防止 __init__ 被多次调用
        if not hasattr(self, "_initialized"):
            self.data = {}  # 初始化数据
            self._initialized = True
            print("初始化单例实例")


# 测试
s1 = SingletonByNew()  # 输出: 创建单例实例\n初始化单例实例
s2 = SingletonByNew()  # 不会再次创建和初始化

s1.data["host"] = "localhost"
print(f"s1.data: {s1.data}")  # 输出: {'host': 'localhost'}
print(f"s2.data: {s2.data}")  # 输出: {'host': 'localhost'}
print(f"是同一个实例: {s1 is s2}")  # 输出: True

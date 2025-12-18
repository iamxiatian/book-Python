import time


class DataProcessor:
    def __init__(self):
        self.items = ["item_" + str(i) for i in range(10000)]
        self.prefix = "processed_"

    def process_without_caching(self):
        """不使用局部变量缓存"""
        result = []
        for i in range(len(self.items)):
            # 每次循环都进行属性查找
            value = self.prefix + self.items[i]
            result.append(value)
        return result

    def process_with_caching(self):
        """使用局部变量缓存"""
        result = []
        # 将属性缓存到局部变量items和prefix中，避免每次循环都进行属性查找
        items = self.items
        prefix = self.prefix
        for i in range(len(items)):
            # 使用局部变量，避免属性查找
            value = prefix + items[i]
            result.append(value)
        return result


def performance_test():
    """性能对比测试"""
    processor = DataProcessor()

    # 测试不使用缓存的版本
    start_time = time.time()
    processor.process_without_caching()
    time_without_caching = time.time() - start_time

    # 测试使用缓存的版本
    start_time = time.time()
    processor.process_with_caching()
    time_with_caching = time.time() - start_time

    print(f"不使用缓存: {time_without_caching:.6f} 秒")
    print(f"使用缓存避免属性查找: {time_with_caching:.6f} 秒")
    print(f"性能提升: {time_without_caching / time_with_caching:.2f}倍")


if __name__ == "__main__":
    performance_test()

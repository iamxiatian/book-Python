import itertools
import sys


def demonstrate_itertools():
    # 1. chain示例：串联多个迭代器
    list1 = ["item_a", "item_b", "item_c"]
    list2 = ["item_d", "item_e", "item_f"]

    # 传统方法：创建新列表
    traditional_chain = list1 + list2

    # itertools方法：惰性求值
    itertools_chain = itertools.chain(list1, list2)

    print(f"传统方法: {traditional_chain}")
    print(f"itertools方法: {list(itertools_chain)}")

    # 2. 内存使用对比
    large_data = range(1000000)

    # 传统方法：创建完整列表
    traditional_list = [x * 2 for x in large_data]
    traditional_memory = sys.getsizeof(traditional_list)

    # itertools方法：使用生成器表达式
    itertools_generator = (x * 2 for x in large_data)
    itertools_memory = sys.getsizeof(itertools_generator)

    print(f"\n传统列表内存: {traditional_memory / 1024 / 1024:.2f} MB")
    print(f"生成器内存: {itertools_memory / 1024:.2f} KB")

    # 3. 使用islice进行分页处理
    print("\n--- 使用islice进行分页 ---")
    all_items = [f"item_{i+1}" for i in range(10)]

    page_size = 3
    for page_num in range(4):
        start = page_num * page_size
        page = list(itertools.islice(all_items, start, start + page_size))
        if page:
            print(f"第{page_num + 1}页: {page}")


if __name__ == "__main__":
    demonstrate_itertools()

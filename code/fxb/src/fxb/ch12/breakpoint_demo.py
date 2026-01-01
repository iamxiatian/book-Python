# file: src/fxb/ch12/breakpoint_demo.py
import traceback
import sys


def my_debugger(*args, **kwargs):
    """自定义调试器函数"""
    print("进入自定义调试器")
    # 调用实际的调试器
    import ipdb

    ipdb.set_trace()


sys.breakpointhook = my_debugger

def process_data(items):
    """ 示例函数，演示breakpoint的使用场景 """
    result = 0
    for item in items:
        if item.get("value") == 0:
            breakpoint()

        result += item["value"]
        result += 100 / item["value"]
    return result


if __name__ == "__main__":
    # 准备测试数据
    data = [
        {"value": 20, "label": "A"},
        {"value": 10, "label": "B"},  # 这个值会触发断点
        {"value": 0, "label": "C"},
    ]
    # 执行调试
    try:
        process_data(data)
    except Exception:
        # 进入事后调试，无需提前在错误位置设置断点...
        traceback.print_exc()
        breakpoint()

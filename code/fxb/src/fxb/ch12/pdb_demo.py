# file: src/fxb/ch12/pdb_demo.py
import ipdb as pdb
#import pudb as pdb
#import pdb
import traceback

def process_data(items):
    """
    示例函数，演示pdb调试器的使用场景
    """
    result = 0
    for item in items:
        # 设置断点，当value等于0时触发
        if item.get("value") == 0:
            pdb.set_trace() 

        # 模拟复杂处理逻辑, 处理到label为"C"时会抛出除以0异常
        result += item["value"]
        result += 100 / item["value"]
        # 在PDB调试会话中，可使用以下命令分析状态：
        # p result     # 查看result变量的结果
        # p locals()   # 查看所有局部变量
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
        pdb.post_mortem() 

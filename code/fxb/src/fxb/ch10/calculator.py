def divide(a, b):
    """安全的除法函数，处理除零错误"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

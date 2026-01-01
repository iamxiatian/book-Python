import debugpy  # 在远程环境中安装并导入 debugpy


def process_data(items):
    """示例函数"""
    result = 0
    for item in items:
        if item.get("value") == 0:
            # 原来设置set_trace()的地方,改为在IDE中设置断点，而非在代码中硬编码。
            print(f"检测到 value 为 0 的项: {item}")

        result += item["value"]
        result += 100 / item["value"]
    return result


if __name__ == "__main__":
    print("应用启动")

    # 启动调试服务器并等待连接
    # 监听所有网络接口(0.0.0.0)的5678端口，这是默认的调试端口
    debugpy.listen(("0.0.0.0", 5678))
    print("调试服务器已启动，等待调试器连接在端口 5678...")

    # 这行会阻塞，直到有IDE连接上来。用于调试启动阶段的问题。
    # 如果只想调试运行中的问题，可以注释掉此行，服务器仍会接受连接，
    # 但程序会立即继续执行。
    debugpy.wait_for_client()
    print("调试器已连接，继续执行主逻辑。")

    data = [
        {"value": 20, "label": "A"},
        {"value": 10, "label": "B"},  # 这个值会触发断点
        {"value": 0, "label": "C"},
    ]
    # 执行调试
    try:
        process_data(data)
    except Exception:
        # 也可以在异常时触发断点 (仅在调试器连接时生效)
        debugpy.breakpoint()  # 程序化断点
    print("应用运行结束")

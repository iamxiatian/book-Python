def process_data(items):
    result = 0
    for item in items:
        if item.get("value") == 0:
            print(f"检测到 value 为 0 的项: {item}")

        result += item["value"]
        result += 100 / item["value"]
    return result

if __name__ == "__main__":
    data = [
        {"value": 20, "label": "A"},
        {"value": 10, "label": "B"},  # 这个值会触发断点
        {"value": 0, "label": "C"},
    ]
    try:
        process_data(data)
    except Exception:
        import traceback
        traceback.print_exc()
    print("应用运行结束")

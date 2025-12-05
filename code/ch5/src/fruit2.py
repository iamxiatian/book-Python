def process_apple(fruit):
    """处理苹果的逻辑, 圈复杂度=3"""
    if not fruit.is_fresh:
        return "坏苹果"

    if fruit.process == "peel":
        return "削皮苹果"
    elif fruit.process == "juice":
        return "苹果汁"
    return "整个苹果"


def process_banana(fruit):
    """处理香蕉的逻辑, 圈复杂度=2"""
    if fruit.ripeness == "ripe":
        return "成熟香蕉"
    elif fruit.ripeness == "green":
        return "青香蕉"
    return "过熟香蕉"


def process_berry(fruit):
    """处理浆果的逻辑, 圈复杂度=2"""
    if fruit.washed:
        return "洗净的" + fruit.type
    return "未清洗的" + fruit.type


# 2. 创建策略注册表(清晰的数据驱动映射)
FRUIT_PROCESSORS = {
    "apple": process_apple,
    "banana": process_banana,
    "strawberry": process_berry,  # 草莓
    "blueberry": process_berry,  # 蓝莓
    # 可轻松扩展新水果
}


# 3. 精简的主协调函数
def process_fruit(fruit):
    """
    主函数, 圈复杂度=2
    职责: 路由分发, 不包含具体业务逻辑
    """
    # 条件1: 检查水果类型是否支持
    processor = FRUIT_PROCESSORS.get(fruit.type)

    # 条件2: 有处理器则调用, 否则返回默认
    if processor:
        return processor(fruit)
    return "其他水果"

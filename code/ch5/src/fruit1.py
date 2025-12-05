def process_fruit(fruit):
    if fruit is None:  # 条件1: 检查水果是否有效
        return "无效水果"

    if fruit.type == "apple":  # 条件2: 检查水果类型
        if fruit.is_fresh:  # 条件3: 检查苹果是否新鲜
            if fruit.process == "peel":  # 条件4: 检查处理方式
                return "削皮苹果"
            elif fruit.process == "juice":  # 条件5: 检查处理方式
                return "苹果汁"
            else:
                return "整个苹果"
        else:
            return "坏苹果"
    elif fruit.type == "banana":  # 条件6: 检查水果类型
        if fruit.ripeness == "ripe":  # 条件7: 检查香蕉是否成熟
            return "成熟香蕉"
        elif fruit.ripeness == "green":  # 条件8: 检查香蕉是否成熟
            return "青香蕉"
        else:
            return "过熟香蕉"
    else:
        # 条件5:检查是否为浆果类
        if fruit.family == "berry":  # 条件9: 检查浆果类
            if fruit.washed:  # 条件10: 检查是否清洗
                return "洗净的" + fruit.type
            else:
                return "未清洗的" + fruit.type
        else:
            return "其他水果"

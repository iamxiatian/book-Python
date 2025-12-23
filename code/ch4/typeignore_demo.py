from typing import List

# 创建一个整数列表的类型注解
items: List[int] = [1, 2, 3]

# 这行代码会导致类型检查错误：尝试向整数列表添加字符串
items.append("string")  # 这里会引发类型错误

# 使用 type: ignore 来抑制类型检查错误
items.append("string")  # type: ignore

# 转换列表中的所有元素为字符串
string_items = [str(item) for item in items]

print(f"字符串列表: {string_items}")

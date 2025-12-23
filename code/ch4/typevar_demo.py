from typing import TypeVar

# 1. 无约束的 TypeVar：可以代表任何类型
T = TypeVar("T")  # 'T' 是类型变量的名称（惯例用单个大写字母）

# 2. 有约束的 TypeVar：只能代表指定类型（比如 int 或 str）
S = TypeVar("S", int, str)  # S 只能是 int 或 str

# 3. 绑定 TypeVar：指定类型变量的上界（即只能是指定类型或其子类）
V = TypeVar("V", bound=int)  # V 只能是 int 或其子类(python中，bool是int的子类)


def first(values: list[V]) -> V:
    return values[0]


# Python 解释器本身不强制执行类型注解，所以这一步不会直接导致程序崩溃,
# 但不符合类型设计的意图。如果用静态检查工具（如 mypy）运行，也会直接提示错误：
print(first(["hello", "world"]))

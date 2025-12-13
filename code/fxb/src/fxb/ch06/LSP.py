from typing import List


# 违反 LSP 的例子
class Bird:
    def fly(self) -> str:
        return "飞行中"

    def eat(self) -> str:
        return "进食中"


class Penguin(Bird):
    def fly(self) -> str:
        # 企鹅不会飞，违反 LSP
        raise NotImplementedError("企鹅不会飞！")


# 遵循 LSP 的重构
class Bird:
    def eat(self) -> str:
        return "进食中"


class FlyingBird(Bird):
    def fly(self) -> str:
        return "飞行中"


class Penguin(Bird):
    def swim(self) -> str:
        return "游泳中"


class Sparrow(FlyingBird):
    def fly(self) -> str:
        return "麻雀在飞行"


def process_birds(birds: List[Bird]):
    """处理鸟类 - 应该能接受任何 Bird 子类"""
    for bird in birds:
        print(bird.eat())
        # 不能调用 fly()，因为不是所有鸟都会飞


def process_flying_birds(birds: List[FlyingBird]):
    """处理会飞的鸟类"""
    for bird in birds:
        print(bird.fly())


# 测试 LSP
def test_lsp():
    birds = [Penguin(), Sparrow()]
    process_birds(birds)  # 正常工作

    flying_birds = [Sparrow()]
    process_flying_birds(flying_birds)  # 正常工作


test_lsp()

# 策略接口：定价策略
class PricingStrategy:
    """定价策略接口"""

    def calculate_price(
        self, fruit: str, quantity: int, base_price: float
    ) -> float:
        pass


# 具体策略类
class SeasonalDiscount(PricingStrategy):
    """季节性折扣策略"""

    def __init__(self, discount_rate: float = 0.1):
        self.discount_rate = discount_rate

    def calculate_price(
        self, fruit: str, quantity: int, base_price: float
    ) -> float:
        return base_price * quantity * (1 - self.discount_rate)


class MemberDiscount(PricingStrategy):
    """会员折扣策略"""

    def __init__(self, member_level: str = "gold"):
        self.discount_rates = {"gold": 0.2, "silver": 0.1, "bronze": 0.05}
        self.discount_rate = self.discount_rates.get(member_level, 0)

    def calculate_price(
        self, fruit: str, quantity: int, base_price: float
    ) -> float:
        return base_price * quantity * (1 - self.discount_rate)


# 上下文类：水果购物车
class FruitShoppingCart:
    """水果购物车，使用策略模式计算总价"""

    def __init__(self, pricing_strategy: PricingStrategy):
        self.items = []
        self.pricing_strategy = pricing_strategy

    def add_item(self, fruit: str, quantity: int, base_price: float):
        self.items.append(
            {"fruit": fruit, "quantity": quantity, "base_price": base_price}
        )

    def calculate_total(self) -> float:
        total = 0.0
        for item in self.items:
            price = self.pricing_strategy.calculate_price(
                item["fruit"], item["quantity"], item["base_price"]
            )
            total += price
        return total

    def set_pricing_strategy(self, strategy: PricingStrategy):
        """动态切换定价策略"""
        self.pricing_strategy = strategy


# 使用策略模式
def test_stragety():
    """演示策略模式的使用"""

    cart = FruitShoppingCart(SeasonalDiscount(0.1))  # 季节性9折
    cart.add_item("苹果", 5, 3.0)
    cart.add_item("香蕉", 3, 2.5)
    print(f"季节性折扣总价: {cart.calculate_total():.2f}元")

    # 切换到会员折扣策略
    cart.set_pricing_strategy(MemberDiscount("gold"))
    print(f"黄金会员折扣总价: {cart.calculate_total():.2f}元")


if __name__ == "__main__":
    test_stragety()

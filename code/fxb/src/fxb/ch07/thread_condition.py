import threading
import time


class FruitInventory:
    """水果库存管理"""

    def __init__(self):
        self.fruits = []
        self.lock = threading.Lock()
        self.has_fruits = threading.Condition(self.lock)  # 条件变量

    def add_fruit(self, fruit):
        """添加水果到库存"""
        with self.lock:
            self.fruits.append(fruit)
            print(f"添加:{fruit}, 库存:{len(self.fruits)}个")
            self.has_fruits.notify()  # 通知等待的线程

    def take_fruit(self):
        """从库存取水果"""
        with self.lock:
            # 如果库存为空，则等待
            while len(self.fruits) == 0:
                print("库存空了，等待进货...")
                self.has_fruits.wait()

            fruit = self.fruits.pop(0)
            print(f"取出:{fruit}, 库存:{len(self.fruits)}个")
            return fruit


def supplier(inventory: FruitInventory):
    """供应商：提供水果"""
    for fruit in ["苹果", "香蕉", "橙子", "葡萄"]:
        time.sleep(1)  # 进货时间
        inventory.add_fruit(fruit)


def customer(inventory: FruitInventory, customer_id:int):
    """顾客：购买水果"""
    for _ in range(2):
        time.sleep(1.5)  # 购买间隔
        fruit = inventory.take_fruit()
        print(f"顾客{customer_id}买到了: {fruit}")


# 创建库存
inventory = FruitInventory()

# 创建1个供应商线程和2个顾客线程
supplier_thread = threading.Thread(target=supplier, args=(inventory,))
customer_threads = [
    threading.Thread(target=customer, args=(inventory, i)) for i in range(1, 3)
]

supplier_thread.start()
for c in customer_threads:
    c.start()

supplier_thread.join()
for c in customer_threads:
    c.join()

print("今日营业结束！")

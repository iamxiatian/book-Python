import threading
import time

# 创建一个事件，表示水果拼盘是否准备好
fruit_plate_ready = threading.Event()


def prepare_fruit_plate():
    """准备水果拼盘"""
    print("厨师正在准备水果拼盘...")
    time.sleep(2)  # 准备时间
    print("水果拼盘准备好了！")
    fruit_plate_ready.set()  # 设置事件，通知顾客


def customer(customer_id):
    """顾客等待水果拼盘"""
    print(f"顾客{customer_id}在等待水果拼盘")
    fruit_plate_ready.wait()  # 等待事件
    print(f"顾客{customer_id}开始享用水果拼盘")


# 创建1个厨师线程和3个顾客线程
chef = threading.Thread(target=prepare_fruit_plate)
customers = [threading.Thread(target=customer, args=(i,)) for i in range(1, 4)]

chef.start()
for c in customers:
    c.start()

chef.join()
for c in customers:
    c.join()

print("所有顾客都享用完毕！")

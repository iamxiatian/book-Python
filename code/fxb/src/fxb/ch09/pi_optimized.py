import random
import math
import numpy as np
import time

def estimate_pi(num_samples):
    """使用蒙特卡洛方法估算丌值"""
    inside_circle = 0

    for _ in range(num_samples):
        x = random.random()
        y = random.random()

        # 检查点是否在单位圆内
        if math.sqrt(x**2 + y**2) <= 1:
            inside_circle += 1

    # 根据面积比例估算丌值
    pi_estimate = 4 * inside_circle / num_samples
    return pi_estimate


def estimate_pi_optimized(num_samples):
    """不依赖sqrt()函数的丌值估算函数"""
    inside_circle = 0

    # 预计算循环条件
    for _ in range(num_samples):
        x = random.random()
        y = random.random()

        # 避免sqrt调用，使用平方比较
        if x * x + y * y <= 1:
            inside_circle += 1

    return 4 * inside_circle / num_samples


def estimate_pi_vectorized(num_samples):
    """使用NumPy向量化计算的丌值估算函数"""
    # 一次性生成所有随机数
    x = np.random.random(num_samples)
    y = np.random.random(num_samples)

    # 向量化计算
    inside_circle = np.sum(x * x + y * y <= 1)

    return 4 * inside_circle / num_samples


def benchmark_pi():
    """性能基准测试"""
    num_samples = 5_000_000
    t1 = time.time()
    estimate_pi(num_samples)
    t2 = time.time()
    estimate_pi_optimized(num_samples)
    t3 = time.time()
    estimate_pi_vectorized(num_samples)
    t4 = time.time()

    print(f"原方法耗时: {t2-t1:.2f}秒")
    print(f"去掉sqrt后耗时: {t3-t2:.2f}秒")
    print(f"采用numpy耗时: {t4-t3:.2f}秒")


if __name__ == "__main__":
    benchmark_pi()

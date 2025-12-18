import time
import math
import pi_cython  # 导入编译好的Cython模块
import random

def estimate_pi_pure(num_samples):
    """纯Python版本的π值计算"""
    inside_circle = 0
    for _ in range(num_samples):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1:
            inside_circle += 1
    return 4 * inside_circle / num_samples


def benchmark():
    """性能基准测试"""
    num_samples = 5_000_000
    print(f"计算π值 - 样本数: {num_samples:,}")
    print("=" * 30)

    # 纯Python版本
    start_time = time.time()
    pi_pure = estimate_pi_pure(num_samples)
    time_pure = time.time() - start_time

    # Cython版本
    start_time = time.time()
    pi_cy = pi_cython.estimate_pi_python(num_samples)
    time_cy = time.time() - start_time

    # 输出结果
    print("纯Python版本:")
    print(f"  估算值: {pi_pure:.8f}")
    print(f"  实际值: {math.pi:.8f}")
    print(f"  误差: {abs(pi_pure - math.pi):.8f}")
    print(f"  耗时: {time_pure:.3f}秒")

    print("\nCython编译版本:")
    print(f"  估算值: {pi_cy:.8f}")
    print(f"  耗时: {time_cy:.3f}秒")

    print(f"\n性能提升: {time_pure / time_cy:.2f}倍")

if __name__ == "__main__":
    benchmark()

import random
import math

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

def benchmark_pi():
    """性能基准测试"""
    import time
    
    num_samples = 5_000_000
    start_time = time.time()
    
    pi_estimate = estimate_pi(num_samples)
    
    elapsed_time = time.time() - start_time
    print(f"丌估算值: {pi_estimate:.6f}")
    print(f"丌实际值: {math.pi:.6f}")
    print(f"误差: {abs(pi_estimate - math.pi):.6f}")
    print(f"耗时: {elapsed_time:.2f}秒")
    print(f"每秒采样数: {num_samples/elapsed_time:,.0f}")

if __name__ == "__main__":
    benchmark_pi()
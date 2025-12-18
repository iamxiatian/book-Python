import random

def estimate_pi_cython(num_samples):
    """Cython版本的π值估算函数"""
    cdef int inside_circle = 0
    cdef int i
    cdef double x, y
    
    for i in range(num_samples):
        x = random.random()
        y = random.random()
        
        # 避免sqrt调用，使用平方比较
        if x * x + y * y <= 1:
            inside_circle += 1
    
    return 4 * inside_circle / num_samples

# 纯Python接口，保持与原始代码兼容
def estimate_pi_python(num_samples):
    """纯Python接口"""
    return estimate_pi_cython(num_samples)
from multiprocessing import Process, Value, Array


# 子进程修改共享内存的函数
def modify_shared(shared_num, shared_arr):
    shared_num.value += 10  # 修改Value需通过.value属性
    for i in range(len(shared_arr)):
        shared_arr[i] *= 2  # Array可直接下标修改


if __name__ == "__main__":
    # 1. 创建共享内存对象
    # Value(类型码, 初始值)：i=int, f=float, b=bool, s=str（需指定长度）
    shared_num = Value("i", 0)  # 共享整数，初始值0
    shared_arr = Array("i", [1, 2, 3])  # 共享整数数组

    # 2. 启动子进程
    p = Process(target=modify_shared, args=(shared_num, shared_arr))
    p.start()
    p.join()

    # 4. 主进程读取共享内存
    print("共享整数：", shared_num.value)  # 输出：10
    print("共享数组：", shared_arr[:])  # 输出：[2,4,6]

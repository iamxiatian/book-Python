from multiprocessing import Process, Manager


# 1. 定义子进程任务：修改共享数据
def modify_manager(shared_dict, shared_list):
    shared_dict["version"] = 3.12
    shared_list.append(40)
    
def test_manager():
    # 2. 创建 Manager 实例（启动服务器进程）
    with Manager() as manager:
        # 2. 创建共享字典和列表
        shared_dict = manager.dict({"name": "Python", "version": 3.10})
        shared_list = manager.list([10, 20, 30])

        # 3. 启动子进程并等待完成
        p = Process(target=modify_manager, args=(shared_dict, shared_list))
        p.start()
        p.join()

        # 4. 主进程中读取被修改后的共享数据
        print(
            "共享字典：", shared_dict
        )  # 输出：{'name': 'Python', 'version': 3.12}
        print("共享列表：", shared_list)  # 输出：[10, 20, 30, 40]

if __name__ == "__main__":
    test_manager()
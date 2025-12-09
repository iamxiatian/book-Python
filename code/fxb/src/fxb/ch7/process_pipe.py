from multiprocessing import Process, Pipe
from multiprocessing.connection import Connection

# 子进程函数：通过管道读写数据
def send_data(conn: Connection):
    conn.send("我不是小白!")  # 发送数据（支持Python任意可序列化对象）
    conn.close()  # 关闭连接

if __name__ == "__main__":
    # 1. 创建管道：返回两个连接对象（conn1, conn2）
    conn1, conn2 = Pipe(duplex=True)  # duplex=True（默认）：双向；False：单向（conn1仅写，conn2仅读）

    # 2. 启动子进程，传入管道一端
    p = Process(target=send_data, args=(conn1,))
    p.start()

    # 3. 主进程通过另一端读取数据
    print(conn2.recv())  # 输出：我不是小白!
    p.join()
    conn2.close()

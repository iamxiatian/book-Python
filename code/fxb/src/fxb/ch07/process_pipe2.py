import multiprocessing
import time
import random


def fruit_inspector(conn, inspector_id):
    """水果检测员进程：检测水果并发送报告"""
    fruit_types = ["苹果", "香蕉", "橙子", "葡萄", "西瓜"]

    for fruit in fruit_types:
        # 模拟检测时间
        time.sleep(random.uniform(0.2, 0.5))
        # 随机生成质量评分（0-100分）
        quality_score = random.randint(70, 100)

        # 发送检测报告
        report = {
            "inspector": inspector_id,
            "fruit": fruit,
            "quality": quality_score,
            "timestamp": time.time(),
        }

        conn.send(report)
        print(f"检测员{inspector_id} 发送报告: {fruit} 质量 {quality_score}分")

        # 等待质量监督员反馈
        feedback = conn.recv()
        print(f"检测员{inspector_id} 收到反馈: {feedback}")

    # 发送结束信号
    conn.send("检测完成")
    conn.close()


def quality_supervisor(conn, supervisor_id):
    """质量监督员进程：接收报告并给出反馈"""
    reports_received = 0

    while True:
        # 接收检测报告
        report = conn.recv()

        if report == "检测完成":
            print(f"监督员{supervisor_id}: 所有检测完成")
            conn.send("收到完成信号")
            break

        reports_received += 1

        # 模拟审核时间
        time.sleep(random.uniform(0.1, 0.3))

        # 根据质量评分给出反馈
        if report["quality"] >= 90:
            feedback = f"{report['fruit']} 质量优秀，可上架特级区"
        elif report["quality"] >= 80:
            feedback = f"{report['fruit']} 质量良好，可上架普通区"
        else:
            feedback = f"{report['fruit']} 质量合格，需降价处理"

        # 发送反馈
        conn.send(feedback)
        print(f"监督员{supervisor_id} 审核第{reports_received}份报告")

    conn.close()


def demo_fruit_pipe():
    # 创建管道，返回两个连接对象
    inspector_conn, supervisor_conn = multiprocessing.Pipe()

    # 创建进程
    inspector = multiprocessing.Process(
        target=fruit_inspector, args=(inspector_conn, 1)
    )

    supervisor = multiprocessing.Process(
        target=quality_supervisor, args=(supervisor_conn, 1)
    )

    print("=== 水果质量检测系统启动 ===")
    # 启动进程
    inspector.start()
    supervisor.start()

    # 等待进程完成
    inspector.join()
    supervisor.join()

    print("=== 质量检测完成 ===")

if __name__ == "__main__":
    demo_fruit_pipe()

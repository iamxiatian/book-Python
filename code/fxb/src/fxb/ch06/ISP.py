from typing import Protocol


# # 违反 ISP - 胖接口
# class Worker(Protocol):
#     def work(self) -> None: ...
#     def eat(self) -> None: ...


# class HumanWorker:
#     def work(self) -> None:
#         print("人类工作")

#     def eat(self) -> None:
#         print("人类进食")


# class RobotWorker:
#     def work(self) -> None:
#         print("机器人工作")

#     def eat(self) -> None:
#         # 机器人不需要进食，但被迫实现
#         raise NotImplementedError("机器人不需要进食")


# 遵循 ISP - 细粒度接口
class Workable(Protocol):
    def work(self) -> None: ...


class Eatable(Protocol):
    def eat(self) -> None: ...


class HumanWorker:
    def work(self) -> None:
        print("人类工作")

    def eat(self) -> None:
        print("人类进食")


class RobotWorker:
    def work(self) -> None:
        print("机器人工作")


# 专门的工作管理器
class WorkManager:
    def __init__(self, worker: Workable):
        self.worker = worker

    def manage_work(self) -> None:
        self.worker.work()


class HumanResources:
    def __init__(self, worker: Eatable):
        self.worker = worker

    def manage_break(self) -> None:
        self.worker.eat()


# 测试 ISP
def test_isp():
    human = HumanWorker()
    robot = RobotWorker()

    work_manager = WorkManager(human)
    work_manager.manage_work()

    work_manager = WorkManager(robot)
    work_manager.manage_work()

    hr = HumanResources(human)
    hr.manage_break()


test_isp()

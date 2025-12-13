from typing import Protocol, List
from abc import ABC, abstractmethod


# ==== 违反 OCP 的设计：通过条件分支硬编码所有类型 ====
class ReportGenerator:
    """违反 OCP - 每次新增报告类型都要修改这个类"""

    def generate_report(self, report_type: str, data: List) -> str:
        if report_type == "csv":
            return self._generate_csv(data)
        elif report_type == "html":
            return self._generate_html(data)
        elif report_type == "json":
            return self._generate_json(data)
        else:
            raise ValueError(f"不支持的报告类型: {report_type}")

    def _generate_csv(self, data: List) -> str:
        return "CSV 报告"

    def _generate_html(self, data: List) -> str:
        return "HTML 报告"

    def _generate_json(self, data: List) -> str:
        return "JSON 报告"


# ==== 遵循 OCP 的设计：通过策略模式实现扩展 ====
class ReportStrategy(Protocol):
    def generate(self, data: List) -> str: ...


class CSVReport:
    def generate(self, data: List) -> str:
        return "CSV 报告"


class HTMLReport:
    def generate(self, data: List) -> str:
        return "HTML 报告"


class JSONReport:
    def generate(self, data: List) -> str:
        return "JSON 报告"


class ExtensibleReportGenerator:
    """遵循 OCP - 可以通过注册新策略来扩展"""

    def __init__(self):
        self._strategies: dict[str, ReportStrategy] = {}

    def register_strategy(self, report_type: str, strategy: ReportStrategy):
        self._strategies[report_type] = strategy

    def generate_report(self, report_type: str, data: List) -> str:
        strategy = self._strategies.get(report_type)
        if not strategy:
            raise ValueError(f"不支持的报告类型: {report_type}")
        return strategy.generate(data)


# 演示OCP的使用方式
class PDFReport:
    def generate(self, data: List) -> str:
        return "PDF报告"


def test_ocp():
    generator = ExtensibleReportGenerator()
    generator.register_strategy("csv", CSVReport())
    generator.register_strategy("html", HTMLReport())
    generator.register_strategy("json", JSONReport())

    # 可以轻松扩展新类型，无需修改现有代码
    generator.register_strategy("pdf", PDFReport())

    data = [1, 2, 3]
    for report_type in ["csv", "html", "pdf"]:
        result = generator.generate_report(report_type, data)
        print(f"{report_type}: {result}")


test_ocp()

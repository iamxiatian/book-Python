import pytest


def safe_divide(a, b):
    """安全除法函数，处理除零异常"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b


# 测试正常除法场景
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5),
        (9, 3, 3),
        (0, 5, 0),
    ],
)
def test_divide_normal(a, b, expected):
    assert safe_divide(a, b) == expected


# 测试异常场景
@pytest.mark.parametrize(
    "a, b",
    [
        (1, 0),
        (5, 0),
    ],
)
def test_divide_by_zero(a, b):
    with pytest.raises(ValueError) as exc_info:
        safe_divide(a, b)
    assert "除数不能为零" in str(exc_info.value)

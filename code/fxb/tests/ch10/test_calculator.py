import pytest

from fxb.ch10.calculator import divide

def test_divide_normal():
    """测试正常除法"""
    result = divide(10, 2)
    assert result == 5


def test_divide_by_one():
    """测试除以1"""
    result = divide(7, 1)
    assert result == 7


def test_divide_zero_by_number():
    """测试0除以某个数"""
    result = divide(0, 5)
    assert result == 0


def test_divide_negative_numbers():
    """测试负数除法"""
    result = divide(-10, 2)
    assert result == -5


def test_divide_by_zero():
    """测试除零异常"""
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert "除数不能为零" in str(exc_info.value)


def test_divide_floats():
    """测试浮点数除法"""
    result = divide(5.5, 2.2)
    assert abs(result - 2.5) < 0.0001  # 使用容差比较浮点数

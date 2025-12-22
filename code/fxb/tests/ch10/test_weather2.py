import requests
from fxb.ch10.weather import get_weather

def test_get_weather_success(mocker):
    """测试场景1：API调用成功（使用pytest-mock）"""
    # 1. 通过mocker.patch创建模拟对象（替代unittest的@patch装饰器）
    mock_get = mocker.patch("requests.get")

    # 2. 配置模拟对象行为（逻辑与unittest.mock完全一致）
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {"temperature": 25.5}

    # 3. 调用被测函数并验证
    result = get_weather("北京")
    assert result == 25.5
    mock_get.assert_called_once_with(
        "https://api.weather.com/city/北京", timeout=5
    )


def test_get_weather_failure(mocker):
    """测试场景2：API返回404（使用pytest-mock）"""
    mock_get = mocker.patch("requests.get")
    mock_response = mock_get.return_value
    mock_response.status_code = 404

    result = get_weather("不存在的城市")
    assert result is None


def test_get_weather_network_error(mocker):
    """测试场景3：网络超时（使用pytest-mock）"""
    mock_get = mocker.patch("requests.get")
    mock_get.side_effect = requests.exceptions.Timeout

    result = get_weather("上海")
    assert result is None

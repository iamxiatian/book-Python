import unittest
from unittest.mock import patch
import requests
from fxb.ch10.weather import get_weather


class TestWeatherAPI(unittest.TestCase):

    @patch("requests.get")  # 临时替换requests.get为模拟对象
    def test_get_weather_success(self, mock_get):
        """测试场景1：API调用成功，返回正确温度"""
        # 1. 模拟成功响应。通过为模拟对象的return_value属性赋值，来模拟返回的响应数据。
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {"temperature": 25.5}

        # 也可以分别复制
        #mock_get.return_value.status_code = 200
        # 模拟requests.get返回值的json()函数返回结果
        # mock_get.return_value.json.return_value = {"temperature": 25.5}

        # 2. 调用被测函数
        result = get_weather("北京")

        # 3. 验证核心逻辑与依赖调用
        self.assertEqual(result, 25.5)  # 验证温度计算正确
        # 验证requests.get被调用时传入了正确的参数
        mock_get.assert_called_once_with(
            "https://api.weather.com/city/北京", timeout=5
        )

    @patch("requests.get")
    def test_get_weather_failure(self, mock_get):
        """测试场景2：API返回非200状态码，返回None"""
        # 配置模拟对象：模拟404失败响应
        mock_response = mock_get.return_value
        mock_response.status_code = 404

        result = get_weather("不存在的城市")
        self.assertEqual(result, None)  # 验证异常场景处理正确

    @patch("requests.get")
    def test_get_weather_network_error(self, mock_get):
        """测试场景3：网络超时异常，返回None"""
        # 配置模拟对象：模拟网络超时异常
        mock_get.side_effect = requests.exceptions.Timeout

        result = get_weather("上海")
        self.assertEqual(result, None)  # 验证异常捕获逻辑正确


# if __name__ == "__main__":
#     unittest.main()

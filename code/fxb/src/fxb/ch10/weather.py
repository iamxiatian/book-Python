import requests


def get_weather(city):
    """调用天气API获取指定城市的温度，失败时返回None"""
    try:
        url = f"https://api.weather.com/city/{city}"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json().get("temperature")
        else:
            return None
    except requests.exceptions.RequestException as e:
        return None


if __name__ == "__main__":
    print(get_weather("北京"))

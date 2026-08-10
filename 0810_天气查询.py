import requests

def get_weather(city_name):
    """
    根据城市名查询实时天气
    :param city_name: 目标城市
    :return: 天气信息字符串
    """
    # 免费天气接口
    url = f"https://wttr.in/{city_name}?format=j1"
    try:
        # 发送网络请求
        res = requests.get(url, timeout=8)
        res.raise_for_status()  # 请求异常直接报错
        data = res.json()

        # 提取温度、体感温度、天气状况
        temp = data["current_condition"][0]["tempC"]
        feel_temp = data["current_condition"][0]["FeelsLikeC"]
        weather_desc = data["current_condition"][0]["weatherDesc"][0]["value"]
        wind = data["current_condition"][0]["windspeedKmph"]

        info = f"""
【{city_name} 实时天气】
气温：{temp} ℃
体感温度：{feel_temp} ℃
天气状况：{weather_desc}
风速：{wind} km/h
        """
        return info
    except Exception as e:
        return f"查询失败：{str(e)}"

if __name__ == "__main__":
    city = input("输入查询天气的城市：")
    result = get_weather(city)
    print(result)
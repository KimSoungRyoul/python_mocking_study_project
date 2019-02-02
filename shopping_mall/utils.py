from datetime import datetime

import requests


def request_weather_api(date: datetime):
    response = requests.get(url="http://www.weather.go.kr/weather/api", params={"date": datetime.day})

from datetime import datetime

import requests


def request_weather_api(date: datetime):
    print('이 프린트 문이 보이면 Mocking 되지 못한것이다.')
    response = requests.get(url="http://www.weather.go.kr/weather/api", params={"date": date.day})

    return response.json()


def send_email(email_contents: str):
    print('진짜로 메일을 전송했습니다.........', email_contents)

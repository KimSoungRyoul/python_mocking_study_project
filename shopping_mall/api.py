from datetime import datetime

from shopping_mall.utils import request_weather_api


def check_shopping_mall_is_open():
    print('외부 날씨 api 를 요청하는 로직이 들어있다.')

    response = request_weather_api(date=datetime.now())

    return response

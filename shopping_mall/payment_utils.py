from http import HTTPStatus

import requests


def request_naver_pay(amount):
    print('----request_naver_pay----------')
    response = requests.get(url="http://api.naver.com/api/v1/payment/~~~~", params={'amount': amount})
    print('response.status_code의 값: ', response.status_code)
    print('respnse.json()의 값', response.json())
    if response.status_code == HTTPStatus.OK:
        return response.json()
    else:
        return 'fail'

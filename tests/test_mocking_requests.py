import unittest
from datetime import datetime, timedelta
from http import HTTPStatus
from unittest.mock import patch, PropertyMock

from shopping_mall import api
from shopping_mall.models import Order, User


class TestWithMocking(unittest.TestCase):

    # 일반적인 목킹

    @patch('shopping_mall.api.request_weather_api', return_value={'temperature': 23.3, 'wind': 3, 'is_rain': 'false'})
    def test_function_mocking(self, request_weather_api_mock):
        result = api.check_shopping_mall_is_open()

        self.assertEqual(result, {'temperature': 23.3, 'wind': 3, 'is_rain': 'false'})

    @patch('shopping_mall.models.request_naver_pay', return_value={'amount': 87000, })
    def test_avoid_real_payment(self, request_naver_pay_mock):
        order = Order()
        self.assertEqual(order.payment.amount, 87000)

    # 디테일한 목킹 with requests
    # https://softwareengineering.stackexchange.com/questions/358160/should-one-test-the-values-of-an-enum-using-unit-tests
    @patch('shopping_mall.payment_utils.requests.get', new_callable=PropertyMock)
    def test_requests_json(self, requests_get_mock):
        requests_get_mock.return_value.json.return_value = {'amount': 70000, }
        requests_get_mock.return_value.status_code = HTTPStatus.OK

        order = Order()
        self.assertEqual(order.payment.amount, 70000)

    # property Mocking
    @patch('shopping_mall.models.User.is_expired_password_period', new_callable=PropertyMock, return_value='목킹당함!!')
    def test_property_mock(self, mock_property):
        user = User()
        user.password_updated_at = datetime.now() - timedelta(days=1)

        self.assertEqual(user.is_expired_password_period, '목킹당함!!')


class TestPropertyMocking(unittest.TestCase):

    def test_mocking_property(self):
        pass

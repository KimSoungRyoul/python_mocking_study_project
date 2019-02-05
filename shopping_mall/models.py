from datetime import datetime
from enum import Enum
from typing import List

from shopping_mall.payment_utils import request_naver_pay


def send_authentication_mail():
    pass


class User(object):
    user_id: str
    password: str
    email: str
    password_updated_at: datetime

    @property
    def is_expired_password_period(self):
        return '비밀번호 변경 아직 안해도 됩니다.' if self.password_updated_at > datetime.datetime.now() else '비번 변경해야됩니다'


class Product(object):
    product_id: int
    name: str
    price: int


class BookType(Enum):
    NOVEL = 'novel'
    IT = 'IT'
    SCIENCE = 'science'


class Book(Product):
    genre: BookType


class PaymentType(Enum):
    CREDIT_CARD = 'credit_card'
    NAVER_PAY = 'naver_pay'


class Payment(object):
    payment_id: int
    amount: int
    payment_type: PaymentType

    def __init__(self, payment_type, amount):
        self.payment_type = payment_type
        self.amount = amount
        if self.payment_type == PaymentType.NAVER_PAY:
            result = request_naver_pay(amount=self.amount)
            self.amount = result['amount']


class Order(object):
    order_id: int
    products: List[Product]
    owner: User
    estimated_delivery_time: datetime
    payment: Payment

    def __init__(self):
        self.payment = Payment(payment_type=PaymentType.NAVER_PAY, amount=10000)

    def is_arrival(self):
        return self.estimated_delivery_time < datetime.now()

    @property
    def product_cnt(self):
        return self.products.count()


class ShopOwner(object):

    def asdf(self, user: User):
        user.asdf

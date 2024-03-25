from django.test import TestCase

from member.models import Member
from order.models import Order


class OrderDetailTestCase(TestCase):
    # 로그인
    # data = {
    #     'member_email': 'zzanggu@naver.com',
    #     'member_password': 'zzzz'
    # }
    #
    # member = Member.enabled_objects.get(**data)

    # 주문 내역(목록)
    # orders = Order.enabled_objects.filter(member=member)
    # for order in orders:
    #     print(order.__dict__)

    # 주문 상세 내역(상세보기)
    # data = {
    #     'id': 3
    # }
    #
    # order = Order.objects.get(**data)
    # order_items = order.orderdetail_set.all()
    #
    # for order_item in order_items:
    #     print(order_item.product.product_sell_price)
    #     print(order.price)
    pass












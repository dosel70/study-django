from django.db import transaction
from django.db.models import Sum, F
from django.test import TestCase
from django.utils import timezone

from cart.models import Cart
from cart_detail.models import CartDetail
from member.models import Member
from order.models import Order
from order_detail.models import OrderDetail
from product.models import Product


class OrderTest(TestCase):
    # # 로그인
    data = {
        'member_email': 'jsh@gmail.com',
        'member_password': '1234'
    }

    member = Member.enabled_objects.get(**data)
    #
    with transaction.atomic():
        # 장바구니
        data = {
            'ids': [1, 3]
        }
    #
        my_cart = Cart.objects.get(status=0, member=member)
        cart_items = CartDetail.objects.filter(cart=my_cart, status=0, id__in=data['ids'])
        price = 0
        for cart_item in cart_items:
            price += cart_item.product.product_sell_price * cart_item.quantity
        print(price)

        # 결제
        data = {
            'member': member,
            'payment': 'card',
            'price': price,
            'delivery_address': '서울특별시 강서구',
        }
        order = Order.objects.create(**data)
        product = Product.sell_price_objects.get(id=2)
        data = {
            'product' : product,
            'quantity': 5
        }
        OrderDetail.objects.create(order=order,**data)
    #
    #     for cart_item in cart_items:
    #         OrderDetail.objects.create(order=order, product=cart_item.product, quantity=cart_item.quantity)
    #         cart_item.status = 1
    #         cart_item.updated_date = timezone.now()
    #         cart_item.save(update_fields=['status', 'updated_date'])
    #
    #     if not CartDetail.objects.filter(cart=my_cart, status=0).exists():
    #         my_cart.status = 1
    #         my_cart.updated_date = timezone.now()
    #         my_cart.save(update_fields=['status', 'updated_date'])

    # 결제 취소
    data = {
        'id' : 1
    }

    order = Order.objects.get(id=2)
    order.status = False
    order.updated_date = timezone.now()
    order.save(update_fields=['status','updated_date'])











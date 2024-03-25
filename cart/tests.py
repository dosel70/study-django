from django.db import transaction
from django.test import TestCase

from cart.models import Cart
from cart_detail.models import CartDetail
from member.models import Member
from product.models import Product


class CartTests(TestCase):
    # # 로그인
    data = {
        'member_email': 'test456@gmail.com',
        'member_password': '1234'
    }
    # #
    member = Member.enabled_objects.get(**data)
    #
    # # 상품 목록
    products = Product.sell_price_objects.all()
    #
    # # 상품 상세페이지
    product = products[2]
    print(product.__dict__)
    #
    # # 장바구니에 상품 추가
    #
    # # 내 장바구니 가져오기
    # my_cart = Cart.objects.filter(status=0, member=member)
    my_cart = Cart.objects.filter(status=0, member=member)
    if not my_cart.exists():
        my_cart = Cart.objects.create(member=member)
    else :
        my_cart = my_cart.first()

    CartDetail.objects.create(cart=my_cart, product=product, quantity=3)
    # if not my_cart.exists(): # 장바구니가 없을 때(장바구니에 상품이 하나도 없을 때)
    #     # 새로운 장바구니를 만들어서 my_cart에 담아준다.
    #     my_cart = Cart.objects.create(member=member)
    # else: # 장바구니가 존재할 때(장바구니에 추가된 다른 상품이 존재할 때)
    #     # 기존 장바구니를 my_cart에 담아준다.
    #     my_cart = my_cart.first()
    #
    # CartDetail.objects.create(cart=my_cart, product=product, quantity=3)

    # 장바구니 목록
    # 상품 정보, 수량
    # data = {
    #     'member_email': 'zzanggu@naver.com',
    #     'member_password': 'zzzz'
    # }
    #
    # member = Member.enabled_objects.get(**data)
    #
    # carts = CartDetail.objects.filter(status=0, cart=Cart.objects.get(member=member, status=0))
    # for cart in carts:
    #     print(cart.product.__dict__)
    #     print(cart.quantity)
    #     print("=" * 30)

    # 장바구니에 담긴 상품 임의로 삭제

    # 오류 발생 시 자동 롤백을 위해 사용하고,
    # 오류가 없으면 커밋된다.
    # @transaction.atomic # 메소드 전체를 하나의 트랜잭션으로 설정
    # def service(self):
    # with transaction.atomic(): # 블록 전체를 하나의 트랜잭션으로 설정
    #     data = {
    #         'member_email': 'zzanggu@naver.com',
    #         'member_password': 'zzzz'
    #     }
    #
    #     member = Member.enabled_objects.get(**data)
    #
    #     my_cart = Cart.objects.get(member=member, status=0)
    #
    #     carts = CartDetail.objects.filter(status=0, cart=my_cart)
    #     cart = carts[0]
    #     cart.status = -1
    #     cart.save(update_fields=['status'])
    #
    #     if not CartDetail.objects.filter(cart=my_cart, status=0).exists():
    #         my_cart.status = -2
    #         my_cart.save(update_fields=['status'])
    pass











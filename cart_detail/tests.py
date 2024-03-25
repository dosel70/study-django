from django.db.models import F
from django.test import TestCase

from cart.models import Cart
from cart_detail.models import CartDetail
from member.models import Member
from product.models import Product


class CartDetailTest(TestCase):
    # product_data = {
    #     'product_name' : '노르웨이 생연어',
    #     'product_price' : 17900,
    #     'product_discount' : 20
    # }
    # products = Product.objects.get(**product_data)
    # cart_data = {
    #     'member_id' : 4
    # }

   pass
    # detail_delete = CartDetail.objects.filter(product__product_name='노르웨이 생연어').update(status=1)
    # print(detail_delete)
    # cart_detail = CartDetail.objects.all().values("product__product_name", "product__product_price", "product__product_discount")
    # cart_detail_count = CartDetail.objects.all().values("product__product_name").count()
    # print(f'상품정보 : {cart_detail},상품 수량 : {cart_detail_count}')


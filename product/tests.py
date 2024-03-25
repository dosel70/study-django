import datetime
import math

from django.db.models import F
from django.db.models.functions import Floor
from django.test import TestCase
from django.utils import timezone

from product.models import Product


class ProductTestCase(TestCase):
    # 상품 추가
    # datas = [
    #     Product(product_name='춘천 국물 닭갈비', product_price=13_200, product_discount=15),
    #     Product(product_name='노르웨이 생연어', product_price=17_900, product_discount=20),
    #     Product(product_name='성주 참외', product_price=25_900, product_discount=11),
    #     Product(product_name='간편 미식 도시락', product_price=5_200, product_discount=20),
    # ]
    #
    # Product.objects.bulk_create(datas)

    # 상품 게시
    # count = Product.objects.all().update(status=True)
    # print(count)
    # products = Product.sell_price_objects.all()

    # print(products)

    # 상품 할인율 적용 가격
    # products = Product.enabled_objects.all().annotate(product_sell_price=Floor(F('product_price') * (1 - F('product_discount') / 100) / 10) * 10)
    # for product in products:
    #     print(product.product_price, product.product_discount, product.product_sell_price)
    #     print("=" * 20)

    # 상품 수정
    # count = Product.objects.filter(id=3).update(product_price=25000, updated_date=timezone.now())
    # print(count)
    pass


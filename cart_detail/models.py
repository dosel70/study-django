from django.db import models

import manage
from cart.models import Cart
from model.models import Period
from product.managers import ProductManager
from product.models import Product


# Create your models here.
class CartDetail(Period):
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT, default=1)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1, null=False)
    status = models.SmallIntegerField(null=False, default=0)
    sell_product_manager = ProductManager()
    class Meta :
        db_table = 'tbl_cart_detail'
        ordering = ['-id']
        base_manager_name = 'sell_product_manager'

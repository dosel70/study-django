from django.db import models

from member.models import Member
from model.models import Period


# Create your models here.
class Order(Period):
    member = models.ForeignKey(Member, on_delete=models.PROTECT)
    payment = models.TextField(blank=False, null=False)
    price = models.BigIntegerField(blank=False, null=False)
    delivery_address= models.TextField(blank=False, null=False)

    # 결제 완료 True , 결제 취소 False
    status = models.BooleanField(blank=False, null=False, default=True)

    class Meta :
        db_table = 'tbl_order'
        ordering = ['-id']

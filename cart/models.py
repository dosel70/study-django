from django.db import models

from member.models import Member
from model.models import Period
# Create your models here.

class Cart(Period):
    CART_STATUS_CHOICES = {
        1 : '결제완료',
        0 : '게시중',
        -1 : '삭제'
    }
    member = models.ForeignKey(Member, on_delete=models.PROTECT, null=False)
    # 게시중 0, 결제 완료 1, 결제 취소 -1
    status = models.SmallIntegerField(null=False ,default=0)

    class Meta :
        db_table = 'tbl_cart'


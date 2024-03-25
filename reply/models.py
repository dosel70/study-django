from django.db import models
from member.models import Member
from model.models import Period
from post.models import Post


# Create your models here.

class Reply(Period):
    SECREAT_STATUS_CHOICES = [ #  상수를 넣는다.
        (True,'비밀글'),
        (False, '일반글')
    ]
    content = models.TextField(blank=False, null=False)
    author = models.CharField(max_length=20)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    member = models.ForeignKey(Member, on_delete=models.PROTECT)
    group_id = models.BigIntegerField(default=1)
    deep = models.IntegerField(null=False, default=1) # 대댓글 수
    secret_reply = models.BooleanField(default=False ,choices = SECREAT_STATUS_CHOICES)

    class Meta:
        ordering = ['-id']
        db_table = 'tbl_reply'

    def __str__(self):
        return self.content

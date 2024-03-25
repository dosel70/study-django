from django.db import models

from alarm.managers import AlarmManager
from member.models import Member
from post.models import Post


class Alarm(models.Model):
    receiver = models.ForeignKey(Member,null=False ,related_name='receiver', on_delete=models.PROTECT)
    sender = models.ForeignKey(Member, null=False , related_name='sender', on_delete=models.PROTECT)
    post = models.ForeignKey(Post,null=False , related_name='post', on_delete=models.PROTECT)
    #: 안읽듬, 1: 읽음 , -1 : 삭제
    status = models.SmallIntegerField(default=0)
    objects = models.Manager()
    enabled_objects = AlarmManager()

    class Meta :
        db_table = 'tbl_alaram'
        ordering = ['-id']





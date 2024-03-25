from django.db import models
from django.db.models import Q, F

from member.models import Member
from model.models import Period


class FriendManager(models.Manager):
    def filter_member(self, member, **kwargs):
        condition_sender = Q(sender=member)
        condition_receiver = Q(receiver=member)

        friends_receiver = super().get_queryset().annotate(friend=F('receiver')).filter(condition_sender, **kwargs)
        friends_sender = super().get_queryset().annotate(friend=F('sender')).filter(condition_receiver, **kwargs)

        friends = friends_sender | friends_receiver
        return friends


class Friend(Period):
    FRIEND_STATUS = [
        (-1, '거절'),
        (0, '대기'),
        (1, '승인')
    ]

    sender = models.ForeignKey(Member, related_name='sender_set', null=False, on_delete=models.PROTECT)
    receiver = models.ForeignKey(Member, related_name='receiver_set', null=False, on_delete=models.PROTECT)
    status = models.SmallIntegerField(choices=FRIEND_STATUS, default=0)
    objects = models.Manager()
    friends_objects = FriendManager()

    class Meta:
        db_table = 'tbl_friend'

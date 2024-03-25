from django.db import transaction
from django.test import TestCase

from alarm.models import Alarm
from member.models import Member
from post.models import Post
from reply.models import Reply
from django.db import transaction

class AlarmTestCase(TestCase):
    with transaction.atomic():
        # 로그인
        data = {
            'member_email': 'kames@gmail.com',
            'member_password': '1234'
        }

        member = Member.objects.get(**data)

        # 게시글 목록
        posts = Post.objects.all()[0:10]

        # 게시글 상세보기
        post = Post.objects.get(id=posts[0].id)

        # 댓글 작성
        data = {
            'content': '테스트 댓글90',
            'post': post,
            'member': member
        }
        reply = Reply.objects.create(**data)
        reply.group_id = reply.id
        reply.save(update_fields=['group_id'])
    #
    #     # 알람 추가
    #     data = {
    #         'receiver': post.member,
    #         'sender': member,
    #         'post': post
    #     }
    #     Alarm.objects.create(**data)

    # 로그인
    data = {
        'member_email': 'qwer@gmail.com',
        'member_password': '1234'
    }

    member = Member.objects.get(**data)

    # 알람 목록
    alarms = Alarm.enabled_objects.filter(receiver=member).values()
    for alarm in alarms:
        print(alarm)

    # 알람 확인
    data = {
        'id': 2
    }
    count = Alarm.enabled_objects.filter(**data).update(status=1)
    print(count)
from django.test import TestCase

from alarm.models import Alarm
from member.models import Member
from post.models import Post
from reply.models import Reply


class AlarmTestCase(TestCase):
    with transaction.atomic():
        # 로그인
        data = {
            'member_email': 'dino1@gmail.comm',
            'member_password': 'zzzz'
        }

        member = Member.objects.get(**data)

        # 게시글 목록
        posts = Post.objects.all()[0:10]

        # 게시글 상세보기
        post = Post.objects.get(id=posts[0].id)

        # 댓글 작성
        data = {
            'reply_content': '테스트 댓글90',
            'post': post,
            'member': member
        }
        reply = Reply.objects.create(**data)
        reply.group_id = reply.id
        reply.save(update_fields=['group_id'])

        # 알람 추가
        data = {
            'receiver': post.member,
            'sender': member,
            'post': post
        }
        Alarm.objects.create(**data)

    # 로그인
    data = {
        'member_email': 'test5@gmail.com',
        'member_password': '1234'
    }

    member = Member.objects.get(**data)

    # 알람 목록
    alarms = Alarm.enabled_objects.filter(receiver=member).values()
    for alarm in alarms:
        print(alarm)

    # 알람 확인
    data = {
        'id': 2
    }
    count = Alarm.enabled_objects.filter(**data).update(status=1)
    print(count)
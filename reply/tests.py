from django.db.models import F
from django.test import TestCase

from member.models import Member
from post.models import Post
from reply.models import Reply


class ReplyTest(TestCase):

    # 댓글 추가
    # member_data = {
    #     'member_email': 'test5@gmail.com',
    #     'member_password': '1234'
    # }
    #
    # member = Member.enabled_objects.get(**member_data)
    # post = Post.objects.get(id=7)
    #
    # reply_data = {
    #     'reply_content': '댓글 테스트2',
    #     'member': member,
    #     'post': post,
    #
    # }
    #
    # reply = Reply.objects.create(**reply_data)
    # reply.group_id = reply.id
    # reply.save()

    # 대댓글 3개 등록하기
    # ※ 실행 3번으로 3개 등록하기
    # member_data = {
    #     'member_email': 'james@gmail.com',
    #     'member_password': '1234'
    # }
    # member = Member.objects.get(**member_data)
    # post = Post.objects.get(id=590)
    # reply = Reply.objects.filter(post_id=post.id, deep=1)[0]
    #
    # re_reply_data = {
    #     'content': '테스트 대댓글3',
    #     'post': post,
    #     'member': member,
    #     'group_id': reply.id,
    #     'deep': 2,
    #     'secret_reply': True
    # }
    #
    # re_reply = Reply.objects.create(**re_reply_data)
    # print(re_reply)
    #
    # replies = Reply.objects.filter(group_id=2)
    # for reply in replies:
    #     print(reply.get_secret_reply_display())
    #
    # member_data = {
    #     'member_email': 'james@gmail.com',
    #     'member_password': '1234'
    # }
    #
    # members = Member.objects.get(**member_data)

    # # 게시글 상세보기
    # # 게시글 정보, 회원 정보, 댓글 목록, 댓글의 대댓글 목록을 출력
    # post_data = {
    #     "post_title" : '테스트제목20',
    #     "member_id" : "2"
    # }

    # 7번 게시글의 내용과 작성자 정보를 가져온다.
    # posts = Post.objects.filter(id=591)\
    #     .annotate(member_name=('member__member_name'))\
    #     .values(
    #     'id',
    #     'post_title',
    #     'post_content',
    #     'member__member_name',
    #     ).first()
    #
    # #게시글에 맞는 정보 룰력
    # replies = Reply.objects.filter(post_id=posts['id'], deep=1)
    # for reply in replies :
    #     print(reply)
    # # 댓글 번호를 전달받은 뒤
    # data ={
    #     'id' : 2
    # }
    # re_replies = Reply.objects.filter(group_id=data['id'], deep=1)
    # for reply in re_replies :
    #     print(reply)
    #
    # 게시글을 작성한 적이 있는 회원 목록 출력
    # members = Member.objects.filter(post__isnull=False).values()
    # for member in members:
    #     print(member)
    #

    # members = Member.objects.filter(reply__deep=2,reply__isnull=False).values('id','reply')
    # for member in members:
    #     print(member)
    #
    # replies = Reply.objects.filter(deep=1).values('id','content','member_id','member__member_email')
    # for reply in replies:
    #     print(reply)

    # members = Member.objects.filter(id=2).values('id','member_name','member_age')
    # for member in members:
    #     print(member)
    # 게시글 상세보기
    # id가 1인 멤버가 작성한 게시글의 첫번째 데이터를 참조하고 있는 댓글 에서 첫번째 댓글만 조회(내용과 비밀글 여부만)
    #     posts = Post.objects.filter(member_id=1).values('member_id', 'member__member_name', 'member__member_status')
    #     for post in posts :
    #         print(post)
    replies = Reply.objects.filter(member_id=1).values('content').first()
    posts = Post.objects.filter(member_id=1)
    for post in posts :
        print(replies)

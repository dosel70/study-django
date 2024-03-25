from django.db import connection
from django.db.models import Q, Count, Model, F, ProtectedError, Max, Min
from django.test import TestCase

from member.models import Member
from post.models import Post
from reply.models import Reply


# class MemberTest(TestCase):
#     # 클래스 내부에 코드를 작성하면 연결한 테이블에 저장되고,
#     # 메소드 내에서 코드를 작성하면 임시 테이블에 저장된 뒤 사라진다.
#     # pass
#     # create
#     member = Member.objects.create(
#         member_email='qwer@gmail.com',
#         member_password='1234',
#         member_age=37,
#         member_name='양양',
#     )


    # print(member.__dict__)
    # def test_member_creation(self):
    #     member = Member.objects.create(
    #         member_email='test1@gmail.com',
    #         member_password='1234',
    #         member_age=20,
    #         member_name='테스트1',clas
    #     )
    #
    #     print(member.__dict__)

    # 회원 1명 추가
    # Member.objects.create()

    # 회원 2명 추가
    # for i in range(2):
    #     Member.objects.create()

    # save
    # datas = {
    #     'member_email': 'test2@gmail.com',
    #     'member_password': '1234',
    #     'member_age': 20,
    #     'member_name': '테스트2',
    # }
    # member = Member(**datas)
    # member.save()

    # 회원 1명 추가
    # datas = {}
    # member = Member(**datas)
    # member.save()

    # 회원 2명 추가
    # datas = [
    #     {},
    #     {},
    # ]
    #
    # for data in datas:
    #     member = Member(**data)
    #     member.save()

    # bulk_create
    # id는 가져오지 않는다.
    # members = Member.objects.bulk_create([
    #     Member(
    #         member_email='test3@gmail.com',
    #         member_password='1234',
    #         member_age=10,
    #         member_name='테스트3'),
    #     Member(
    #         member_email='test4@gmail.com',
    #         member_password='1234',
    #         member_age=30,
    #         member_name='테스트4'),
    #     Member(
    #         member_email='test5@gmail.com',
    #         member_password='1234',
    #         member_age=40,
    #         member_name='테스트5')
    # ])
    #
    # for member in members:
    #     print(member.__dict__)

    # 회원 2명 추가
    # datas = [
    #     {},
    #     {}
    # ]
    #
    # members = []
    #
    # for data in datas:
    #     members.append(Member(**data))
    #
    # Member.objects.bulk_create(members)

    # get_or_create
    # datas = {
    #     'member_password': '1234',
    #     'member_age': 50,
    #     'member_name': '테스트6',
    # }
    # member, created = Member.objects.get_or_create(member_email='test6@gmail.com', defaults=datas)
    # print(member.__dict__, created)

    # member_email이 'admin1@gmail.com'인 회원을 조회한다.
    # 만약 없으면 새로운 정보를 전달하여 회원을 추가한다.
    # datas = {}
    #
    # member, isCreated = Member.objects.get_or_create(member_email='admin1@gmail.com', defaults=datas)

    # get
    # member = Member.objects.get(id=3)
    # print(member.__dict__)

    # all
    # members = Member.objects.all()
    # members = Member.enabled_objects.all()
    # for member in members:
    #     print(member.__dict__)

    # filter
    # member_queryset = Member.enabled_objects.filter(member_name='테스트6')
    # print(member_queryset.exists())
    # print(member_queryset[0].__dict__)

    # 로그인된 회원의 상세페이지에서 내가 등록한 맵주소 찾기
    # data = {
    #     'member_email': 'test4@gmail.com',
    #     'member_password': '1234'
    # }
    #
    # member = Member.enabled_objects.get(**data)
    # print(member.member_name)

    # 게시글과 댓글을 모두 작성한 회원을 찾으세요
    # 화면 예시
    # 회원 정보, 게시글 개수, 댓글 개수
    # query = """
    #     select m_p.id, m_p.member_email, m_p.member_name, m_p.post_count, count(r.id) reply_count
    #     from
    #     (
    #         select m.id, m.member_email, m.member_name, count(p.id) post_count
    #         from tbl_member m left outer join tbl_post p
    #         on m.id = p.member_id
    #         group by m.id, m.member_email, m.member_name
    #     ) m_p left outer join tbl_reply r
    #     on m_p.id = r.member_id
    #     group by m_p.id, m_p.member_email, m_p.member_name, m_p.post_count
    # """
    # cursor = connection.cursor()
    # cursor.execute(query)
    # members = cursor.fetchall()
    # descriptions = cursor.description
    # members_list = []
    #
    # for member in members:
    #     members_dict = {}
    #     for i in range(len(descriptions)):
    #         description, *rest = descriptions[i]
    #         members_dict[description] = member[i]
    #     members_list.append(members_dict)
    #
    # for member in members_list:
    #     print(member)

    # members_post = Member.objects.values(
    #     'id',
    #     'member_email',
    #     'member_name',
    # ).annotate(post_count=Count('post'))
    #
    # members_reply = Member.objects.values(
    #     'id',
    #     'member_email',
    #     'member_name',
    # ).annotate(reply_count=Count('reply'))
    #
    # for i in range(len(members_post)):
    #     members_post[i]['reply_count'] = members_reply[i]['reply_count']
    #
    # for member_post in members_post:
    #     print(member_post)

    # 회원 이름이 "테스트6"이거나 회원 나이가 30이상인 회원이 작성한 게시글 목록 조회
    # name_condition = Q(member_name='테스트6')
    # age_condition = Q(member_age__gte=30)
    # condition = name_condition | age_condition
    #
    # members = Member.objects.filter(condition).values()
    # for member in members:
    #     print(member)

    # condition = Q()
    #
    # condition |= name_condition
    # condition |= age_condition

    # search
    #
    # data = {
    #     'region': '',
    #     'color': '검은색',
    #     'date': '2019-05-01'
    # }
    # region_condition = Q(region=data['region'])
    # color_condition = Q(color=data['color'])
    #
    # condition = Q()
    # if data.region:
    #     condition &= region_condition
    #
    # if data.color:
    #     condition &= color_condition
    #
    # Post.objects.filter(condition)

    # range
    # 회원의 나이가 20이상 30이하인 회원이 작성한 게시글 중 post_title에 "테"가 들어가고 내용에 "7"로 끝나는 게시글 정보 조회
    # members = Member.objects.filter(
    #     member_age__range=[20, 30],
    #     post__post_title__contains='테',
    #     post__post_content__endswith='7'
    # ).values('member_age', 'post__post_title', 'post__post_content')
    #
    # for member in members:
    #     print(member)

    # posts = Post.objects.filter(
    #     member__member_age__range=[20, 30],
    #     post_title__contains='테',
    #     post_content__endswith='7'
    # ).values('member__member_age', 'post_title', 'post_content')
    #
    # for post in posts:
    #     print(post)

    # contains
    # member_queryset = Member.enabled_objects.filter(member_name__contains='테')
    # print(member_queryset.exists())
    # for member in member_queryset:
    #     print(member.__dict__)

    # startswith, endswith
    # member_queryset = Member.enabled_objects.filter(member_name__startswith='테')
    # print(member_queryset.exists())
    # for member in member_queryset:
    #     print(member.__dict__)
    # member_queryset = Member.enabled_objects.filter(member_name__endswith='3')
    # print(member_queryset.exists())
    # for member in member_queryset:
    #     print(member.__dict__)

    # in
    # member_queryset = Member.enabled_objects.filter(member_email__in=['test3@gmail.com', 'test6@gmail.com']).values('member_email')
    # print(member_queryset.query)
    # for member in member_queryset:
    #     print(member.get('member_email'))

    # exclude()
    # member_queryset = Member.enabled_objects.exclude(member_email='test3@gmail.com').values('member_email')
    # for member in member_queryset:
    #     print(member["member_email"])

    # AND, OR
    # member_queryset = Member.objects.filter(status=True) & Member.objects.filter(member_age__gt=30)
    # condition1 = Q(status=True)
    # condition2 = Q(member_age__gt=30)
    # member_queryset = Member.objects.filter(condition1 & condition2)
    # member_queryset = Member.objects.filter(condition1 | condition2)
    # for member in member_queryset:
    #     print(member.member_email, member.member_age, sep=", ")

    # order_by
    # member_queryset = Member.objects.all().order_by('-id')
    # for member in member_queryset:
    #     print(member.__dict__)

    # save
    # # 회원 이름 수정
    # data = {
    #     'member_email': 'test2@gmail.com',
    #     'member_password': '3333'
    # }

    # member = Member.objects.get(**data)
    # member.member_name = '수정된 이름'
    # member.member_password = '3333'
    # member.save(update_fields=['member_name'])

    # member = Member.objects.filter(**data)
    # count = member.update(member_name='다시 수정된 이름')
    # print(count)

    # count = Member.objects.update(member_name='수정된 이름')
    # print(count)

    # 나이가 20살 이하인 회원의 나이를 +1한다.
    # count = Member.objects.filter(member_age__lte=20).update(member_age=F('member_age') + 1)
    # print(count)

    #delete :
    # try :
    #     count = Member.objects.get(id__gt=150).delete()
    #     print(count)
    # except ProtectedError :
    #     print('ProtectedError')
    #
    # # aggpregate
    # # annotate()는 QuerySet 객체로 리턴하기 때문에, 이어서 추가 작업이 가능하지만,
    # # aggregate()는 전체 대상이므로 뒤에 이어서 추가 작업이 불가능하다.
    # member = Member.objects.aggregate(max_age=Max('member_age'), min_age = Min('member_age'))
    # print(member['max_age'], member['min_age'])


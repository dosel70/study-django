from django.db.models import Q
from django.test import TestCase

from friend.models import Friend
from member.models import Member


class FriendTest(TestCase):
    data = {
        'member_email': 'shin@gmail.com',
        'member_password': 'ssss',
        'member_name': '신형만',
        'member_age': 39
    }

    Member.objects.create(**data)
    #
    # data = {
            #'member_email':'zzanga@gmail.com',
            #'member_password':'zzzz'
    # }
    # sender = Member.objects.get(**data)
    #
    # data = {
    #     'member_email': 'yuri@hanmail.net'
    # }
    #
    # receiver = Member.objects.get(member_email=data['member_email'])
    #
    # Friend.objects.create(sender=sender, receiver=receiver)

    # 친구 요청 조건(False일 때에만 요청 가능)
    # data = {
    #     'member_email': 'yuri@hanmail.net'
    # }
    #
    # receiver = Member.objects.get(member_email=data['member_email'])
    #
    #
    # condition_exist = Q(receiver=receiver, sender=sender)
    # condition_status = Q(status=1) | Q(status=0)
    # condition = condition_exist & condition_status
    #
    # condition = Friend.objects.filter(condition).exists()
    # print(condition)

    # 친구 목록
    data = {
        'member_email': 'zzanga@gmail.com',
        'member_password': 'zzzz'
    }

    # # 로그인한 회원
    member = Member.objects.get(**data)

    # 친구 요청을 보냈거나 받은 목록에서
    condition_sender = Q(sender=member)
    condition_receiver = Q(receiver=member)
    condition = condition_sender | condition_receiver

    #############################################################################
    # 친구 수락이 된 정보 모두 조회
    friends = Friend.friends_objects.filter_member(member, status=True)
    for friend in friends:
        print_id = Friend.objects.filter(id=friend.id).update(status=-1)
        print(friend.friend)
    #############################################################################

    # members = Friend.enabled_objects.filter(condition, status=True)
    # friends = []
    # for friend in members:
    #     # 로그인한 회원이 아닌 상대 회원 정보 추출
    #     friends.append(friend.sender if friend.sender.id != member.id else friend.receiver)
    #
    # # 내 친구 목록
    # print(friends)
    #
    # for friend in friends:
    #     print(friend.__dict__)

    # 친구 삭제: 상태가 1인 친구들
    # 친구 거절: 상태가 0인 친구들
    # data = {
    #     'member_email': 'yuri@hanmail.net',
    #     'member_password': 'yyyy'
    # }
    #
    # member = Member.objects.get(**data)
    #
    # data = {
    #     'member_email': 'zzanggu@naver.com',
    # }
    #
    # friend = Member.objects.get(**data)
    #
    # Friend.friends_objects.filter_member(member, friend=friend.id, status=1).update(status=-1)

    # 친구 수락
    # data = {
    #     'member_email': 'yuri@hanmail.net',
    #     'member_password': 'yyyy'
    # }
    #
    # receiver = Member.objects.get(**data)
    #
    # data = {
    #     'member_email': 'hoon@gmail.com'
    # }
    #
    # sender = Member.objects.get(**data)
    #
    # Friend.objects.filter(sender=sender, receiver=receiver, status=0).update(status=True)

#!-----------------------------------실습(TASK)------------------------------------------------------!
    # # '봉미선'이라는 멤버 추가
    # # data = {
    # #     'member_email': 'bong@gmail.com',
    # #     'member_password': 'bbbb',
    # #     'member_name': '봉미선',
    # #     'member_age': 5
    # # }
    # # Member.objects.create(**data)
    #
    # # 친구 요청
    # data = {
    #     'member_email': 'zzanga@gmail.com',
    #     'member_password': 'zzzz'
    # }
    # # >> 짱아가 친구 요청을 보낸다.
    # sender = Member.objects.get(**data)
    # # 트러블 슈팅 => (멤버 이름이 '훈이'인 경우 현재 tbl_member에 중복된 이름으로 되어 있기 때문에, get()으로 받아 올 수 없었다.
    # # 해결 => 새로 '봉미선'이라는 멤버를 추가하여, tbl_member에 중복되지 않은 새로운 회원을 추가하니 문제 해결완료.
    #
    # data = {
    #     'member_email': 'bong@gmail.com'
    # }
    # receiver = Member.objects.get(member_email=data['member_email'])
    # # >> 봉미선이 친구 요청을 받는다.
    # # Friend.objects.create(sender=sender, receiver=receiver)
    # # Friend 모델에 요청자와 수신자를 받아온다.
    # # 결과 = tbl_friend 에는 현재 요청자(sender=(id: 166 , 짱아) receiver =(id : 167, 봉미선))값이 담긴다.
    # #---------------------friend 모델의 친구 추가 기능 설정 완료-------------------------------------#
    # # 친구 요청 조건 기능 구현 (FRIEND_STATUS 값이 0일때만 추가 가능 확인 용도)
    #
    # # 위에서 전달받은 sender , receiver를 AND,OR 쿼리문을 사용하기 위해 key : value 값을 받아온다. => condition_exist
    # condition_exists = Q(sender=sender, receiver=receiver)
    #
    # # condition_sttus -> Friend 모델의 status 값이 1 또는 0 인지 확인 해본다.
    # condition_status = Q(status=1) | Q(status=0)
    #
    # # condition = 위에서 작성한 condition_exist , condition_status 값을 모두 담는다. (즉 후에 필터를 하기 위해서
    # # 변수로 지정한 것이다.)
    # condition = condition_exists & condition_status
    # # Friend 모델에서 이제 위에서 지정한 condition을 검증한다. 즉 status,exist의 값을
    # # Friend 모델에서 확인 하여 검증하는 것이다. 즉 (status의 default 값이 1인지 0 인지 검증)
    #
    # condition = Friend.objects.filter(condition).exists()
    # # <뒤에 (exists():존재 여부 확인 함수)를 붙힌 이유도 위 조건을 만족하는 객체가 하나라도 있으면 True, 없으면 False 를 반환하는것이다.
    # # *****(뭔가 잘못된 설명, 강사님께 검증 필요)******>
    #
    #
    # print(condition)
    # status 값이 선언되었다는 것을 True를 출력함으로써 확인이 되었다.

    #----------------------------------친구 요청 조건 확인 완료--------------------------------#

    # 실제 로그인한 회원을 대상으로 친구 요청 목록을 확인 해본다.
    # data = {
    #     'member_email':'zzanga@gmail.com',
    #     'member_password' : 'zzzz'
    # }
    # sender = Member.objects.get(**data)
    # print(f'이메일 : {sender.member_email} 비번 : {sender.member_password} 이름 : {sender.member_name}')
    # # 짱아 로그인 등록 완료
    #
    # varify = Friend.objects.filter(sender_id=sender.id).count()
    # print(varify) # 친구 요청자 목록에 '짱아'가 있다는것을 카운트 결과값 1로 확인 완료
    #
    # data = {
    #     'member_email': 'bong@gmail.com',
    # }
    # receiver = Member.objects.get(member_email=data['member_email'])
    # print(receiver.member_name) # 친구 수신자 목록에 '봉미선'이 있다는것을 확인 완료

    # 친구 요청을 보냈거나 받은 목록에서
    # condition_sender = Q(sender=member)
    # condition_receiver = Q(receiver=member)
    # condition = condition_sender | condition_receiver

    #############################################################################
    # 친구 수락이 된 정보 모두 조회
    # friends = Friend.friends_objects.filter_member(member, status=True)
    # for friend in friends:
    #     print(friend.friend)
    #############################################################################
    pass

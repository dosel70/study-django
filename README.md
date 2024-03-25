# study-django

Framework
	라이브러리란, 개발자가 작성해놓은 코드 파일을 의미하며,
	API란, 여러 라이브러리가 모여있는 압축파일을 의미한다.
	Framework란, API가 굉장히 많이 모여져서 덩치가 커져있는 것을 의미한다.

Framework 장점
	개발에 필요한 구조를 이미 코드로 만들어 놓았기 때문에 실력이 부족한 개발자라 하더라도
	반쯤 완성된 상태에서 필요한 부분을 조립하는 형태의 개발이 가능하다.
	회사 입장에서는 Framework를 사용하면 일정한 품질이 보장되는 결과물을 얻을 수 있고,
	개발자 입장에서는 완성된 구조에 자신이 맡은 서비스에 대한 코드를 개발해서 넣기 때문에
	개발 시간을 단축할 수 있다.

Django Framework
	파이썬으로 만들어진 오픈 소스 웹 애플리케이션 프레임워크이며,
	빠르고 쉽게 웹 사이트를 개발할 수 있는 구성 요소로 이루어진 웹 프레임워크이다.

Django Framework의 특징
	1. MVT 패턴
		Model: 테이블에 저장되어 있는 데이터를 불러온 뒤 담아놓는 역할
		View: 테이블에 접근한 뒤 화면에서 사용할 Model객체를 완성시킨다.
		Templates: 클라이언트에게 보여질 화면 구성, 전달받은 Model객체를 사용한다.		

	2. 강력한 ORM
		ORM(Object Relational Mapping)은 객체 관계 매핑이며,
		객체 진영과 RDB 진영의 구조 차이를 자동으로 해결해주는 기술의 총칭이다.
		오로지 객체를 중심으로 설계가 가능하며, 직접 SQL문을 작성하지 않아도
		자동으로 쿼리가 생성되어 실행된다.

	3. 자체 템플릿 지원
		HTML에서 연산이 가능하도록 도와주며, 자체 템플릿 태그가 있기 때문에
		동적인 페이지를 구성할 수 있게 해준다.

	4. 소스코드 변경 감지
		.py 파일의 소스코드가 변경된다면, 이를 자동으로 감지하여 서버를 재시작해준다.

	5. WAS에 종속적이지 않은 환경
		서버를 실행하지 않아도 기능별 단위 테스트가 가능하기 때문에
		버그를 줄이고 개발 시간을 단축할 수 있다.

Django Framework의 장점
	1. 확장성
		객체를 기억하여 재사용할 수 있는 캐싱과 코드 재사용 기능으로 인해 확장성이 좋다.

	2. 보안
		개발자가 SQL 주입, CSRF 공격 및 XSS와 같은 많은 보안 문제를 피할 수 있도록 도와준다.

	3. 기본 라이브러리를 통한 빠른 개발
		처음부터 코드를 작성하는 대신 여러 기능을 포함하는 패키지를 활용할 수 있다.

Django Framework의 목적
	간단한 웹 앱을 제작하거나 Python을 필요로 하는 서비스들을 가볍게 제작하여,
	MSA로 나누어 개발하는 목적으로 사용된다.
	

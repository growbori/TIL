버전2_영화

- 로그인을 먼저 생성 안할경우 makemigrations 할때 오류가 발생!
- migration 했던 내용을 다 지우고 다시 migration 하기!
1. 인덱스 페이지 생성

- INDEX, 회원가입, 로그인 생성
- CREATE해서 영화 내용들을 적을 경우 정보를 받아와서 Display 하기

2. 회원가입 페이지 생성

- CustomerUserCreationForm 활용해서 회원가입 페이지 생성
- 생성 완료될 경우 movie: index 페이지로 전송되도록 설정

3. 로그인 페이지 생성

- AuthenticationForm 활용해서 로그인 페이지 생성
- 생성 완료될 경우 movie: index 페이지로 전송되도록 설정
- if, elsel문을 사용해서 로그인시 메인 페이지의 네비게이션바에 다른 문자가 나타나도록 설정

4. 로그아웃 생성

- from django.contrib.auth import logout as auth_logout 활용해서 클릭시 로그아웃 되도록 설정
- 로그아웃 후 movie 메인 페이지로 전송되도록 설정

5. create 생성

- label과 input을 활용하여 데이터 받기
- csrf를 사용해야 함
- 다 완성될 경우 detail 페이지로 넘어가서 세부 내용이 나오게 해야 한다.
- 메인 페이지로 돌아갈 수 있는 페이지 생성

6. detail 생성

- create에서 생성된 내용 받아오기
- update, delete 버튼 만들어서 기능 생성하기

7. update 생성

- 파일 수정할 수 있게 생성

8. delete 생성

- 파일 제거할 수 있게 생성
- 제거 후 메인 페이지로 돌아가기

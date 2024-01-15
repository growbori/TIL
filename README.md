# SSAFY 11기 Chat GPT 챗봇 프로그래밍
---
## Remote Repository
> 리모트 저장소
-  리모트 저장소는 인터넷이나 네트워크 어딘가에 있는 저장소를 말한다. 저장소는 여러 개가 있을 수 있는데 어떤 저장소는 읽고 쓰기 모두 할 수 있고 어떤 저장소는 읽기만 가능할 수 있다.
>원격 저장소
- 코드와 버전 관리 이력을 온라인 상의 특정 위치에 저장하여 여러 개발자가 협업하고 코드를 공유할 수 있는 공간
>리모트 저장소 서비스
- Gitlab, Github, Bitbucket

## 로컬 & 원격 저장소

> git remote add origin remote_repo_url
- 로컬 저장소에 원격 저장소 주소 추가
> git remote
- 등록된 원격 저장소 목록 확인
![이미지](https://velog.velcdn.com/images/lurelight/post/bff9e74f-f080-4086-80c3-731cf770c3eb/image.png)
> fetch or pull 
- 조회해서 가져오다 (원격 저장소에서 로컬 데이터로 가져옴)
> push
- 밀어낸다 (로컬 데이터를 원격 저장소로 옮김)

git fetch 명령은 리모트 저장소의 데이터를 모두 로컬로 가져오지만, 자동으로 Merge 하지 않는다. 그래서 당신이 로컬에서 하던 작업을 정리하고 나서 수동으로 Merge 해야 한다. 그러나 그냥 쉽게 git pull 명령으로 리모트 저장소 브랜치에서 데이터를 가져올 뿐만 아니라 자동으로 로컬 브랜치와 Merge 시킬 수 있다

> git push -u origin master
- 원격 저장소에 commit 목록을 업로드
![](https://velog.velcdn.com/images/lurelight/post/2ae753f8-93b7-4dbe-9733-547ec45ac00c/image.png)
"git아 push 해줘 origin이라는 이름의 원격 저장소에 master라는 이름의 브랜치를"

> git push

![](https://velog.velcdn.com/images/lurelight/post/4ee7e889-2426-405e-8b52-46130c1c313a/image.png)
![](https://velog.velcdn.com/images/lurelight/post/6f857949-60f4-400a-94b2-3889d7414518/image.png)

git log --oneline에서 확인했을 때, 내가 작성한 3개의 commit이 모두 나타나야 한다.
commit 내역을 상세하게 보면 어떤 변경사항인지 확인할 수 있다.

> git clone remote_repo_url
- 원격 저장소 전체를 복제(다운로드)
clone 으로 받은 프로젝트는 이미 **git init**, **git add**가 이미 포함 되어 있음
clone 발생 시 git init을 할 필요가 없음
![](https://velog.velcdn.com/images/lurelight/post/f3f3724b-85f1-4ddf-897d-40753d5e2c8a/image.png)
로컬에서 파일 명을 변경할 수도 있다.

>코드 내용 (VS code 활용) - 저녁메뉴 git으로 공유하며 메뉴 추가하기
1. 내 컴퓨터에 폴더 생성하기
2. git 에서 repositories 생성하고 repositories 링크 생성하기
![](https://velog.velcdn.com/images/lurelight/post/0c2232b8-42fb-4a01-8183-dab358f91853/image.png)
>>- A(나)가 먼저 폴더, git 만들고 B에게 공유
```
git init # git 설정 초기화
touch 삼겹살.txt # 메뉴 추가
git add 삼겹살.txt # git 을 생성한 사실을 스토리지에 추가
git status # git 상태 확인
git commit -m 'Dinner' # Dinner 안에 메뉴 commit
git log --oneline # 진행 내용 한줄로 정리
git remote add origin https://github.com/growbori/Dinner.git #git과 원격 저장소 서로 연결
git push -u origin master # git에서 작성한 내용 원격 저장소에 업로드
####B 가 메뉴 작성
git pull https://github.com/growbori/Dinner.git # 내가 만든 파일이므로 clone이 아닌 pull을 사용해서 b가 작성한 내용까지 가져오기
touch 카레.txt # 내가 메뉴 또 추가
git add 카레.txt
git commit -m 'Dinner'
git remote add origin https://github.com/growbori/Dinner.git
git push -u origin master
```
>>- B(다른사람)이 먼저 폴더, git 만들고 A(나)에게 공유
```
git clone https://github.com/HongchanAhn/wordchain.git # B가 만든 git 파일을 복사해오기
#받은 코드에서 code 열기
touch 키위새.txt
git add 키위새.txt
git commit -m 'wordchain'
git log
git remote add origin https://github.com/HongchanAhn/wordchain.git # 원격 저장소와 연결
git push -u origin master # 저장한 데이터를 원격 저장소에 전송 
```
![](https://velog.velcdn.com/images/lurelight/post/b1d93652-bd53-47a1-a97d-66a9b2a8bba0/image.png)

git log를 확인했을때 파일 생성자와 파일을 받은 사람의 데이터를 확인할 수 있음
### gitignore
> **gitignore**
- Git에서 특정 파일이나 디렉토리를 추적하지 않도록 설정하는데 사용되는 텍스트 파일
1. .gitignore 파일 생성 (파일명 앞에 '.' 입력, 확장자 없음)
2. a 와 b 이름을 가진 텍스트 파일 생성
3. gitignore 에 a.txt 생성
4. git init
5. git status
>
#### **gitignore 주의사항**
이미 git의 관리를 받은 파일이나 디렉토리는 나중에 gitignore에 작성해도 적용되지 않음
>
gitignore 사용할 때 보면 좋은 사이트
https://www.toptal.com/developers/gitignore/

### github 활용
> **git hub 활용**
TIL(Today I Learned)을 통해 내가 학습하는 것을 기록
개인, 팀 프로젝트 코드를 공유
개발 면접 지원 시 본인의 github 주소를 공유해 어떤 프로젝트들을 진행했고, 어떤 코드를 작성했는지 공유하고 평가 받기 위해 사용
오픈 소스 프로젝트에 기여

> **실습 1 - TIL 만들기**
1. TIL이라는 이름의 Github Repository 생성하기
2. 로컬 저장소 설정
3. README.md 생성 및 지금까지의 수업 내용을 정리하고 commit을 설정
4. TIL 원격 저장소를 추가
5. commit 목록을 push

```
git init # 설정 초기화
git add . # 변경사항 더하기
git commit -m 'README.md' # 변경한 내용 커밋하기
git push https://github.com/growbori/TIL.git # 내 github로 발송!
```
> README.md
- 프로젝트에 대한 설명, 사용 방법, 문서화된 정보 등을 포함하는 역할
- Markdown 형식으로 작성되며, 프로젝트의 사용자, 개발자 혹은 기여자들에게 프로젝트에 대한 전반적인 이해와 활용 방법을 제공하는데 사용
- 주로 프로젝트의 소개, 설치 및 설정 방법, 사용 예시, 라이선스 정보, 기여 방법 등을 포함함
- 반드시 저장소 최상단에 위치해야 원격 저장소에서 올바르게 출력됨

# Python

### **프로그램(Program)**
---
>**프로그램 (Program)**
명령어들의 집합
>
**프로그램 예시**
친구에게 우리 집으로 오는 길을 적어주는 것 -> '프로그램 작성'
적어준 길을 순서대로 따라가는 것 -> '프로그램 실행'
프로그램은 이처럼 몇 가지 기초 연산으로 구성됨
컴퓨터는 더 다양한 연산 집합을 가짐
>
> **프로그래밍의 핵심**
새 연산을 정의하고 조합해 유용한 **작업을 수행**하는 것
**문제를 해결하는 매우 강력한 방법**

### **프로그래밍 언어**
---
>**프로그래밍 언어**
컴퓨터에게 작업을 지시하고 문제를 해결하는 도구

> **파이썬을 사용하는 이유**
간결하고 읽기 쉬운 문법
다양한 응용 분야 - 데이터 분석, 인공지능, 웹 개발, 자동화 등
파이썬 커뮤니티의 지원 - 세계적인 규모의 풍부한 온라인 포럼 및 커뮤니티 생태계

> **파이썬 프로그램이 실행되는 법**
- 컴퓨터는 기계어로 소통하기 때문에 사람이 기계어를 직접 작성하기 어려움
![](https://velog.velcdn.com/images/lurelight/post/c0452352-5646-4308-b8ae-10b5d048ef70/image.png)
>
>
- 인터프리터가 사용자의 명령어를 운영체제가 이해하는 언어로 바꿈
![](https://velog.velcdn.com/images/lurelight/post/fed8509e-d1bd-48c8-9b9b-04bf8e6a9fa8/image.png)

> **파이썬 인터프리터를 사용하는 2가지 방법**
1.  shell 이라는 프로그램으로 한 번에 한 명령어씩 입력해서 실행
![](https://velog.velcdn.com/images/lurelight/post/46a73bff-343a-40ce-85a8-071383bdfea8/image.png)
>
2. 확장자가 .py인 파일에 작성된 파이썬 프로그램을 실행
![](https://velog.velcdn.com/images/lurelight/post/6e5ac1a0-43f5-41c0-984c-bb8f792dc56f/image.png)

### **표현식과 값**
---

>**표현식 (Expression)**
값, 변수, 연산자 등을 조합하여 계산되고 결과를 내는 코드 구조
![](https://velog.velcdn.com/images/lurelight/post/93a47d62-187a-4936-bd6a-6b566d16ceb2/image.png)
표현식이 평가되어 반영됨
**평가 (Evaluate)**
표현식이나 문장을 실행하여 그 결과를 계산하고 값을 결정하는 과정
→ 표현식이나 문장을 순차적으로 평가하여 프로그램의 동작을 결정
**문장 (Statement)**
실행 가능한 동작을 기술하는 코드 (조건문, 반복문, 함수 정의 등)
![](https://velog.velcdn.com/images/lurelight/post/81cdbe7f-f5eb-4d52-a7e1-9feeebf9f613/image.png)
**타입 (Type)**
값이 어떤 종류의 데이터인지 어떻게 해석되고 처리되어야 하는지를 정의
![](https://velog.velcdn.com/images/lurelight/post/e5923d4c-0710-45b3-9fd6-537f0c810295/image.png)
![](https://velog.velcdn.com/images/lurelight/post/5677378c-0f80-41cc-9800-c0ed3dc98c27/image.png)

### **연산자**
---
>**산술연산자**
![](https://velog.velcdn.com/images/lurelight/post/89ca010d-81c4-4ad2-8e27-29daf6b11b68/image.png)
**연산자 우선순위**
![](https://velog.velcdn.com/images/lurelight/post/70c82cee-057b-4d6d-81a3-9d9bcca9d0c4/image.png)

### **변수와 메모리 "값이 저장되는 법"
---
>**변수(Variable)**
값을 **참조**하는 이름
![](https://velog.velcdn.com/images/lurelight/post/1f52467a-1088-431d-a06f-373eb2df42b8/image.png)
>**변수명 규칙**
>>- 영문 알파벳, 언더 스코어 (_), 숫자로 구성
- 숫자로 시작할 수 없음
- 대소문자를 구분
- 파이썬의 내부 예약어는 사용할 수 없음
>
> **변수, 값 그리고 메모리**
거리에 집 주소가 있듯이 메모리의 모든 위치에는 그 위치를 고유하게 식별하는 메모리 주소가 존재
변수는 그 변수가 참조하는 객체의 메모리 주소를 가짐
변수 degrees 는 값 36.5를 참조
>>**객체(Object)**
타입을 갖는 메모리 주소 내 값
'값이 들어있는 상자'
>
>>**할당문**
할당 연산자(=) 오른쪽에 있는 표현식을 평가해서 값(메모리 주소)을 생성
값의 메모리 주소를 '=' 왼쪽에 있는 변수에 저장
존재하지 않는 변수라면 → 새로운 변수를 생성
기존에 존재했던 변수라면 → 기존 변수를 재사용해서 변수에 들어있는 메모리 주소를 변경
![](https://velog.velcdn.com/images/lurelight/post/280cc14a-5fa3-4e43-aa24-23f0ada1d91c/image.png)
















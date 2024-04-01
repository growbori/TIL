### **Authentication System 2**
---

**회원 가입**

User 객체를 Create 하는 과정

**UserCreationForm()**

회원 가입 시 사용자 입력 데이터를 받는 built-in ModelForm

![](https://velog.velcdn.com/images/lurelight/post/a5b97135-1499-4f76-aeb1-20f0737d3de1/image.png)

![](https://velog.velcdn.com/images/lurelight/post/3527b9ae-9d8a-445c-b1c5-098a7eb13e66/image.png)

![](https://velog.velcdn.com/images/lurelight/post/b1b8ac18-805c-436b-a1b3-de5f4473f85a/image.png)

![](https://velog.velcdn.com/images/lurelight/post/661722c4-7c70-4237-9616-dd98ef4ff305/image.png)

![](https://velog.velcdn.com/images/lurelight/post/49e13ec8-874e-48e9-8a7f-6fcdbaeb4302/image.png)

![](https://velog.velcdn.com/images/lurelight/post/75591c52-d6e2-42a7-901a-8c940f7f2717/image.png)

![](https://velog.velcdn.com/images/lurelight/post/347bf9c4-0146-40d5-8438-643e3b803bd7/image.png)

**get_user_model()**

'현재 프로젝트에서 활성화된 사용자 모델 (active user model)'을 반환하는 함수

user객체를 직접적으로 가져오지 않음

![](https://velog.velcdn.com/images/lurelight/post/cecaceee-300b-45f8-aa8a-fa4c35accdde/image.png)

![](https://velog.velcdn.com/images/lurelight/post/bef3c7e7-308c-437c-82ba-d6d4caffb055/image.png)

### **회원 탈퇴**
---

**회원 탈퇴**

User 객체를 Delete 하는 과정

![](https://velog.velcdn.com/images/lurelight/post/6ca2fabf-d3fe-410a-95f8-d5c8b46c5487/image.png)

![](https://velog.velcdn.com/images/lurelight/post/d074cd4f-e6b8-4bd3-a931-5f86063b83a9/image.png)

### **회원정보 수정**
---

**회원정보 수정**

User 객체를 Update 하는 과정

**UserChangeForm()**

회원정보 수정 시 사용자 입력 데이터를 받는 built-in ModelForm

![](https://velog.velcdn.com/images/lurelight/post/bd063f58-6495-4da3-a79e-4e9c0994aca1/image.png)

![](https://velog.velcdn.com/images/lurelight/post/1b93f3ae-590a-4234-a80b-903bd0f6293f/image.png)

![](https://velog.velcdn.com/images/lurelight/post/c8173c14-a65d-47ee-bba3-d224ac4b49e4/image.png)

**UserChangeForm 사용 시 문제점**

User 모델의 모든 정보들 (fields)까지 모두 출력되어 수정이 가능하기 때문에 일반 사용자들이 접근해서는 안되는 정보는 출력하지 않도록 해야 함

→ CustomUserChangeForm에서 접근 가능한 필드를 다시 조정

![](https://velog.velcdn.com/images/lurelight/post/e922189e-44a5-4955-8a63-5373be7d5fe7/image.png)

![](https://velog.velcdn.com/images/lurelight/post/829f2dab-4459-4975-964d-8bce749b651b/image.png)

![](https://velog.velcdn.com/images/lurelight/post/f6d1ba49-fbba-4ad7-87f1-c40f7bd4f940/image.png)

### **비밀번호 변경**
---

**비밀번호 변경**

인증된 사용자의 Session 데이터를 Update 하는 과정

**PasswordChangeForm()**

비밀번호 변경 시 사용자 입력 데이터를 받는 built-in Form

![](https://velog.velcdn.com/images/lurelight/post/eccb34d6-1cd7-47a1-bc27-1d8359b67e17/image.png)

![](https://velog.velcdn.com/images/lurelight/post/2a1687a1-c1b2-49dd-959e-f33f72fbd132/image.png)

![](https://velog.velcdn.com/images/lurelight/post/fd4dc7c2-766c-48cb-9c10-fcdd32c1320a/image.png)

![](https://velog.velcdn.com/images/lurelight/post/425413b7-5890-4dac-8894-a7b1e3ee7d27/image.png)

### **세션 무효화 방지하기**
---

**암호 변경 시 세션의 무효화**

비밀번호가 변경되면 기존 세션과의 회원 인증 정보가 일치하지 않게 되어 버려 로그인 상태가 유지되지 못하고 로그아웃 처리됨

비밀번호가 변경되면서 기존 세션과의 회원 인증 정보가 일치하지 않기 때문

**update_session_auth_hash(request, user)**

암호 변경 시 세션 무효화를 막아주는 함수

→ 암호가 변경되면 새로운 password의 Session Data로 기존 session을 자동으로 갱신

![](https://velog.velcdn.com/images/lurelight/post/9995a5fa-09a1-4881-afc8-d59b522c165d/image.png)

### **인증된 사용자에 대한 접근 제한**
---

**로그인 사용자에 대해 접근을 제한하는 2가지 방법**

1. is_authenticated 속성 (attribute)

2. login_required 데코레이터 (decorator)

**is_authenticated**

사용자가 인증 되었는지 여부를 알 수 있는 User model의 속성

→ 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성이며, 비인증 사용자에 대해서는 항상 False

![](https://velog.velcdn.com/images/lurelight/post/cb55ab3e-2bae-4d34-ab11-f5f2c492bfe6/image.png)

![](https://velog.velcdn.com/images/lurelight/post/e6476bab-f0c3-4860-aea8-d035837b8229/image.png)

**login_required**

인증된 사용자에 대해서만 view 함수를 실행시키는 데코레이터

→ 비인증 사용자의 경우 /accounts/login 주소로 redirect 시킴

![](https://velog.velcdn.com/images/lurelight/post/1a015ace-e6b3-43fd-9c70-d8f7bfee27e7/image.png)

![](https://velog.velcdn.com/images/lurelight/post/551ee7ee-ef12-4cbb-98d2-ac87f4f11c65/image.png)

### **참고**
---

![](https://velog.velcdn.com/images/lurelight/post/a3f2ccb2-ca44-443a-b710-c2380c97b6a5/image.png)

![](https://velog.velcdn.com/images/lurelight/post/95b19c08-9293-42e8-bb71-9abd5e109d4b/image.png)

![](https://velog.velcdn.com/images/lurelight/post/53b858a7-4db1-4be7-a818-8d31b6d5a188/image.png)

![](https://velog.velcdn.com/images/lurelight/post/62b21583-f976-410c-bd76-7eaee56fc996/image.png)

![](blob:https://velog.io/e07b4a63-28b9-4e60-a3ad-830172f4ebd3)


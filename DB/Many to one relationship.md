### **Many to one relationships**
---

**Many to one relationships**

한 테이블의 0 개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 관계

Comment(N) - Article(1)

0개 이상의 댓글은 1개의 게시글에 작성될 수 있다.

![](https://velog.velcdn.com/images/lurelight/post/d9d313b8-5ab1-444f-a0c1-58544c111562/image.png)

![](https://velog.velcdn.com/images/lurelight/post/ff063d96-7e08-4c11-ae98-9ac1ff2ab082/image.png)

커멘트에 외래키가 입력 되어야 어느 게시글에 댓글이 달린 것인지 알 수 있음

### **댓글 모델**
---

**Foreignkey()**

N:1 관계 설정 모델 필드

**댓글 모델 정의**

Foreignkey 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형으로 작성하는 것을 권장

외래키는 Foreignkey 클래스를 작성하는 위치와 관계없이 테이블 필드 마지막에 작성됨

![](https://velog.velcdn.com/images/lurelight/post/2bd1acb8-d049-4250-883a-d584f87610ad/image.png)

![](https://velog.velcdn.com/images/lurelight/post/dc656d91-ad6f-403f-9c6e-c0f5dfb6cfff/image.png)

![](https://velog.velcdn.com/images/lurelight/post/88d105ad-4c35-47d1-930d-d8a54c445ddd/image.png)

![](https://velog.velcdn.com/images/lurelight/post/5b34e148-960a-4942-ac43-8f927dea8b0c/image.png)

![](https://velog.velcdn.com/images/lurelight/post/e96bad3e-81a2-410e-8925-ea15e85a6ba8/image.png)

### **댓글 생성 연습**
---

![](https://velog.velcdn.com/images/lurelight/post/5ee22c0a-a37e-49eb-83ad-6cfd52939afc/image.png)

![](https://velog.velcdn.com/images/lurelight/post/af2ca962-47ce-4284-967c-08b52a8d5665/image.png)

![](https://velog.velcdn.com/images/lurelight/post/86b11139-88d1-46cf-9779-8d423441cfd0/image.png)

![](https://velog.velcdn.com/images/lurelight/post/4fd9c950-29d2-460d-b5bd-4f3b1d576b04/image.png)

![](https://velog.velcdn.com/images/lurelight/post/2f66672b-a6a0-4dd1-9ed3-2c1c05acafe8/image.png)

![](https://velog.velcdn.com/images/lurelight/post/565a6ba8-85ab-40a2-86a0-0b61e18ade33/image.png)

![](https://velog.velcdn.com/images/lurelight/post/3fb37cb7-0a9d-4371-bee9-2568ef5f1ae4/image.png)

### **관계 모델 참조**
---

**역참조**

N:1 관계에서 1에서 N을 참조하거나 조회하는 것

→ N은 외래 키를 가지고 있어 물리적으로 참조가 가능하지만 1은 N에 대한 참조 방법이 존재하지 않아 별도의 역참조 기능이 필요

![](https://velog.velcdn.com/images/lurelight/post/70185ac2-5e0a-4926-b17e-faab68b9a165/image.png)

Comment → Article (참조)

어떤 댓글이 작성된 게시글의 정보

Article → Comment (역참조)

어떤 게시글에 작성된 댓글 목록

**related manager**

N: 1 혹은 M:N 관계에서 역참조 시에 사용하는 매니저

→ 'objects' 매니저를 통해 QuerySet API 를 사용했던 것 처럼 related manager를 통해 QuerySet API를 사용할 수 있게 됨

![](https://velog.velcdn.com/images/lurelight/post/8cd839b1-25f6-430f-89c4-96ed778df1e2/image.png)

![](https://velog.velcdn.com/images/lurelight/post/90403047-5556-4a6e-a1b5-07633745f809/image.png)

![](https://velog.velcdn.com/images/lurelight/post/fc7e4beb-ff83-4d7f-8af0-f6748ecb392d/image.png)

### **댓글 구현**
---

**CREATE**

![](https://velog.velcdn.com/images/lurelight/post/fea5024a-3cfe-4fdb-bc94-07885806fab5/image.png)

![](https://velog.velcdn.com/images/lurelight/post/1230ad3e-e883-46f1-b7c9-e1ec1c352841/image.png)

![](https://velog.velcdn.com/images/lurelight/post/330d063f-4579-43e0-9d3c-37cf4c199ce3/image.png)

![](https://velog.velcdn.com/images/lurelight/post/81fa81bb-516e-40be-a198-eb7b761ea786/image.png)

![](https://velog.velcdn.com/images/lurelight/post/d2e13ce6-af6e-4ee2-8d69-c5fd4c3e9ab0/image.png)

![](https://velog.velcdn.com/images/lurelight/post/18e4c09c-bba5-4fdf-ade2-517b24200b45/image.png)

![](https://velog.velcdn.com/images/lurelight/post/f1d6ed3a-da4b-468d-9d77-be8bcfdc8c9d/image.png)

![](https://velog.velcdn.com/images/lurelight/post/7cbfdf7d-e597-46ba-9286-c66cdca42e0a/image.png)

save(commit = False)

DB에 저장하지 않고 인스턴스만 반환

(Create, but don't save the new instance)

저장이 이루어지기 전에 comment 인스턴스를 제공받는게 필요
Save 메서드의 commit 속성

![](https://velog.velcdn.com/images/lurelight/post/3debe867-ffcd-4b93-bb4f-8c5f91b1d158/image.png)

![](https://velog.velcdn.com/images/lurelight/post/75adee73-f7c7-4521-bcf1-4ed1456ad369/image.png)

### **READ**
---

![](https://velog.velcdn.com/images/lurelight/post/2b5b2e82-b5e3-4901-bc57-8206dfdf5a2d/image.png)

![](https://velog.velcdn.com/images/lurelight/post/27c68805-4e27-45be-9496-9a31e9785d46/image.png)

### **DELETE**
---

![](https://velog.velcdn.com/images/lurelight/post/4f7689c7-7093-4258-a440-81ad6c91f1e7/image.png)

![](https://velog.velcdn.com/images/lurelight/post/d16a4388-4b63-429f-ae29-6a5637fb82a7/image.png)

![](https://velog.velcdn.com/images/lurelight/post/056a9b60-b128-4d9d-bae5-5a22a339479c/image.png)

![](https://velog.velcdn.com/images/lurelight/post/5c39771c-e257-4454-98b0-fd9c9e48a491/image.png)

### **참고**
---

NoReverseMatch 오류가 발생할 경우 현재 페이지의 url 태그만 확인하면 됨

![](https://velog.velcdn.com/images/lurelight/post/50f84d73-6895-4243-95d6-5348c4798ede/image.png)

![](https://velog.velcdn.com/images/lurelight/post/82a5e4b3-4121-4c01-ae52-498c53400427/image.png)

![](https://velog.velcdn.com/images/lurelight/post/fd17999e-acd3-4a4a-bba5-7f29b4035309/image.png)


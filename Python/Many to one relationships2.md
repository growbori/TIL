### **Many to one relationships**
---

**User와 다른 모델 간의 모델 관계 설정**

1. User & Article

2. User & Comment

**Article(N) - User(1)**

0 개 이상의 게시글은 1명의 회원에 의해 작성될 수 있다.

**Comment(N) - User(1)**

0 개 이상의 댓글은 1명의 회원에 의해 작성될 수 있다.

### **Article & User**

**모델 관계 설정**

![](https://velog.velcdn.com/images/lurelight/post/372c9ef0-c53d-4b83-a1ed-bb28ad61b014/image.png)

**User 모델을 참조하는 2가지 방법**

get_user_model()

settings.AUTH_USER_MODEL

![](https://velog.velcdn.com/images/lurelight/post/c9a3c832-ff7d-4bc2-bb05-e6876fbcb59f/image.png)

**Migration**

![](https://velog.velcdn.com/images/lurelight/post/c0bf80fd-db92-48fc-bfb8-f090ba176ae9/image.png)

![](https://velog.velcdn.com/images/lurelight/post/c6c94b99-d135-4c1d-8738-e85d7f7243a8/image.png)

![](https://velog.velcdn.com/images/lurelight/post/24fefb1f-7ba7-4765-956d-5cb6ac60115e/image.png)

![](https://velog.velcdn.com/images/lurelight/post/5563d371-ac09-45a8-841a-30690761eb68/image.png)

### **게시글 CREATE**
---

![](https://velog.velcdn.com/images/lurelight/post/a69b2168-4d2c-43b6-a1da-78750cf4a8f6/image.png)

![](https://velog.velcdn.com/images/lurelight/post/7d830a9a-0893-4f6d-9b82-82d9de167fee/image.png)

![](https://velog.velcdn.com/images/lurelight/post/6294ff88-109c-4a73-b9da-b4a7342360b3/image.png)

![](https://velog.velcdn.com/images/lurelight/post/99d44873-46c0-4983-ad4c-71f57388eeb5/image.png)

![](https://velog.velcdn.com/images/lurelight/post/db22b940-262d-4102-a8de-91c29c42a372/image.png)

### **게시글 READ**
---

![](https://velog.velcdn.com/images/lurelight/post/cd45bee9-e43f-4c69-a2f6-999ae8d121fa/image.png)


![](https://velog.velcdn.com/images/lurelight/post/2b1a27c0-c7f0-4697-a098-c9f890531a4e/image.png)

### **게시글 UPDATE**
---

![](https://velog.velcdn.com/images/lurelight/post/e0ef2c83-b019-423b-979a-5b0d6039159d/image.png)

![](https://velog.velcdn.com/images/lurelight/post/f5a86e8c-a238-4837-96d7-4788b92ad480/image.png)

### **게시글 DELETE**
---

![](https://velog.velcdn.com/images/lurelight/post/213a95c0-0b81-47bf-b807-1db6af94ce55/image.png)

### **Comment & User**
---

**모델 관계 설정**

![](https://velog.velcdn.com/images/lurelight/post/ae28c81d-b623-4182-aace-fc5a983ed59e/image.png)

![](https://velog.velcdn.com/images/lurelight/post/58a9b365-db17-49ee-96c9-7385e5c4843a/image.png)

![](https://velog.velcdn.com/images/lurelight/post/786af2a6-82b8-47b7-b38a-c3238a30591b/image.png)

### **댓글 CREATE**
---

![](https://velog.velcdn.com/images/lurelight/post/d241d593-df21-4c0b-b932-779bc9fa7047/image.png)

![](https://velog.velcdn.com/images/lurelight/post/6c4d2b97-46cb-472d-9aa0-1530cd062b16/image.png)

![](https://velog.velcdn.com/images/lurelight/post/c3f10ab3-8279-4300-bfa0-960a259edff8/image.png)

### **댓글 READ**
---

![](https://velog.velcdn.com/images/lurelight/post/bad1f1e1-a22d-47cc-b644-b9ee2e43d575/image.png)

### **댓글 DELETE**
---

![](https://velog.velcdn.com/images/lurelight/post/4f3435e1-2eea-4659-ad21-f4d4f1c2657b/image.png)

![](https://velog.velcdn.com/images/lurelight/post/f6e8cc9a-df88-4e2e-a690-851595c3d668/image.png)

### **참고**
---

![](https://velog.velcdn.com/images/lurelight/post/64eab476-64b7-4f84-8942-2bbcfd2f7a06/image.png)
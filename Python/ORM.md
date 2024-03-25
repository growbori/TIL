### **ORM**
---

**ORM (Object - Relational - Mapping)**

객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 기술

![](https://velog.velcdn.com/images/lurelight/post/27cf04bd-e502-45ff-b956-e7f9827fd765/image.png)

![](https://velog.velcdn.com/images/lurelight/post/9628f5db-7ad6-4703-a21c-7d8adaaef8c7/image.png)

### **QuerySet API**
---

**QuerySet API**

ORM에서 데이터를 검색, 필터링, 정렬 및 그룹화 하는데 사용하는 도구

→ API를 사용하여 SQL이 아닌 Python 코드로 데이터를 처리

![](https://velog.velcdn.com/images/lurelight/post/d4c70454-1b6a-4f4b-a11b-9d5a6af56fd7/image.png)

![](https://velog.velcdn.com/images/lurelight/post/ee2835ad-fc2d-4234-9077-18985e41e9ef/image.png)

![](https://velog.velcdn.com/images/lurelight/post/aec27179-7410-4b08-bfc7-3d458e6d78ce/image.png)

**Query**

데이터베이스에 특정한 데이터를 보여달라는 요청

퀴리문을 작성한다. → 원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드를 작성한다.

파이썬으로 작성한 코드가 ORM에 의해 SQL로 변환되어 데이터베이스에 전달되며, 데이터베이스의 응답 데이터를 ORM이 QuerySet이라는 자료 형태로 변환하여 우리에게 전달

**QuerySet**

데이터베이스에서 전달받은 객체 목록 (데이터 모음)

- 순회 가능한 데이터로써 1개 이상의 데이터를 불러와 사용할 수 있음

Django ORM을 통해 만들어진 자료형

단, 데이터베이스가 단일한 객체를 반환할 때는 QuerySet이 아닌 모델(Class)의 인스턴스로 반환됨

QuerySet API 는 python의 모델 클래스와 인스턴스를 활용해 DB에 데이터를 저장, 조회, 수정, 삭제 하는 것

### **QuerySet API 실습**
---

**Create**

![](https://velog.velcdn.com/images/lurelight/post/72021ebf-a826-465e-a665-035f10d23280/image.png)

**Django shell**

Django 환경 안에서 실행되는 python shell (입력하는 QuerySet API 구문이 Django 프로젝트에 영향을 미침)

![](https://velog.velcdn.com/images/lurelight/post/13c8412b-6f9e-442e-a425-01688acc7b91/image.png)

![](https://velog.velcdn.com/images/lurelight/post/94284555-a5ca-4d6f-a443-2677947be01e/image.png)

![](https://velog.velcdn.com/images/lurelight/post/4eef280f-af1c-430d-8b03-1a791aebcf5a/image.png)

![](https://velog.velcdn.com/images/lurelight/post/f2195179-2d56-4cde-ab3c-bf842c184c0d/image.png)

![](https://velog.velcdn.com/images/lurelight/post/e4a85abd-1a78-4457-ba9e-8dfefc1777f8/image.png)

![](https://velog.velcdn.com/images/lurelight/post/addbce07-1da1-4af3-8ea2-fa1bdc87e944/image.png)

**save()**

객체를 데이터베이스에 저장하는 메서드

### **Read**
---

**대표적인 조회 메서드**

Return new QuerySets

- all()

- filter()

Do not return QuerySets

- gets()

![](https://velog.velcdn.com/images/lurelight/post/ee38f6dc-7614-4552-9e55-af20c175b8a3/image.png)

![](https://velog.velcdn.com/images/lurelight/post/7d39b1b8-7af2-4795-8946-93b6cc577368/image.png)

![](https://velog.velcdn.com/images/lurelight/post/a260a87a-e404-4813-8088-4da387e0636f/image.png)

**get() 특징**

객체를 찾을 수 없으면 DoesNotExist 예외를 발생시키고, 둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외를 발생시킴

→ 위와 같은 특징을 가지고 있기 때문에 primary key와 같이 고유성(uniqueness)을 보장하는 조회에서 사용해야 함

### **Update()**
---

![](https://velog.velcdn.com/images/lurelight/post/b2544207-2b69-4cc6-b9aa-328dde7d0145/image.png)

### **Delete**
---

![](https://velog.velcdn.com/images/lurelight/post/5232a83f-82d5-4c90-b001-cd42e964ea13/image.png)

### **참고**
---

**Field lookups**

특정 레코드에 대한 조건을 설정하는 방법

QuerySet 메서드, filter(), exclude() 및 get()에 대한 키워드 인자로 지정

![](https://velog.velcdn.com/images/lurelight/post/63e6010d-1658-4052-b1e0-6ae22bb0ac1a/image.png)

**ORM, QuerySet API를 사용하는 이유**

데이터베이스 쿼리를 추상화하여 Django 개발자가 데이터베이스와 직접 상호작용하지 않아도 되도록 함

데이터베이스와의 결합도를 낮추고 개발자가 더욱 직관적이고 생산적으로 개발할 수 있도록 도움




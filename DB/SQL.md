### **Database**
---

**데이터베이스**

체계적인 데이터 모음

**데이터**

저장이나 처리에 효율적인 형태로 변환된 정보

![](https://velog.velcdn.com/images/lurelight/post/155d82b1-2604-4890-94f9-71d47fdfbec4/image.png)

![](https://velog.velcdn.com/images/lurelight/post/b13c2244-4507-49ac-ba74-750defa556e0/image.png)

데이터를 저장하고 잘 관리하여 활용할 수 있는 기술이 중요해짐

→ 우리가 알고있는 데이터 저장 방식은 어떤 것이 있을 까?

**기존의 데이터 저장 방식**

1. 파일(File) 이용

2. 스프레드 시트(Spreadsheet) 이용

**1. 파일을 이용한 데이터 관리**

어디서나 쉽게 사용 가능

데이터를 구조적으로 관리하기 어려움

**2. 스프레드 시트를 이용한 데이터 관리**

테이블의 열과 행을 사용해 데이터를 구조적으로 관리 가능

![](https://velog.velcdn.com/images/lurelight/post/184f56a1-fa59-4122-88bc-ff3a747a6b7f/image.png)

**스프레드 시트의 한계**

크기 - 일반적으로 약 100만 행 까지만 저장 가능

보안 - 단순히 파일이나 링크 소유 여부에 따른 단순한 접근 권한 기능 제공

정확성 - 공식적으로 '강원'지명이 '강언'으로 바뀌었다면 테이블의 모든 위치에서 해당 값을 업데이트 해야함. 데이터가 시트에 분산되어 있다면 변경에 누락이 생기거나 추가 문제가 발생할 수 있음

**데이터베이스 역할**

데이터를 저장하고 조작 (CRUD)

### **Relational Database**
---

**데이터베이스 역할** 

데이터를 저장(구조적)하고 조작

**관계형 데이터베이스**

데이터 간에 관계가 있는 데이터 항목들의 모음

테이블, 행, 열의 정보를 구조화하는 방식

서로 관련된 데이터 포인터를 저장하고 이에 대한 액세스를 제공 

![](https://velog.velcdn.com/images/lurelight/post/846676ff-cfa7-4be5-8fb0-9d8be1a6572f/image.png)

**관계**

여러 테이블 간의 (논리적) 연결

![](https://velog.velcdn.com/images/lurelight/post/709c2445-cb69-4563-8452-0def8d4af776/image.png)

![](https://velog.velcdn.com/images/lurelight/post/823b0fdb-8117-4cde-b7e8-512061976560/image.png)

![](https://velog.velcdn.com/images/lurelight/post/f850c4f6-471e-4479-a8f5-d71cca2907a5/image.png)

![](https://velog.velcdn.com/images/lurelight/post/fa10e7b0-2e4d-4de6-81b4-6c63e4ba34cc/image.png)

![](https://velog.velcdn.com/images/lurelight/post/6887c99c-14c7-4c83-abe0-8111fac4253e/image.png)

![](https://velog.velcdn.com/images/lurelight/post/90af7eb0-212f-4ae7-8c82-110011984183/image.png)

![](https://velog.velcdn.com/images/lurelight/post/08b368c7-3a18-404c-8f24-9de67ba492c5/image.png)

![](https://velog.velcdn.com/images/lurelight/post/42e72a00-6b01-4ed6-901e-ba2f2fbbe231/image.png)

![](https://velog.velcdn.com/images/lurelight/post/48c6fb4a-be83-4921-9217-47a48f29d1fa/image.png)

![](https://velog.velcdn.com/images/lurelight/post/e45270ac-14e1-4006-bf3f-36fd25b16808/image.png)

![](https://velog.velcdn.com/images/lurelight/post/1352f075-5c54-4cc2-9b68-fd27519ca3c3/image.png)

### **RDBMS**
---

**DBMS (Database Management System)**

데이터베이스를 관리하는 소프트웨어 프로그램

데이터 저장 및 관리를 용이하게 하는 시스템

데이터베이스와 사용자 간의 인터페이스 역할

사용자가 데이터 구성, 업데이트, 모니터링, 백업, 복구 등을 할 수 있도록 도움

**RDBMS (Relational Database Management System)**

관계형 데이터베이스를 관리하는 소프트웨어 프로그램

![](https://velog.velcdn.com/images/lurelight/post/334f5390-bb2d-4fea-9806-2ca33960a6a4/image.png)

**SQLite**

경량의 오픈 소스 데이터베이스 관리 시스템

→ 컴퓨터나 모바일 기기에 내장되어 간단하고 효율적인 데이터 저장 및 관리를 제공

데이터베이스 정리

Table은 데이터가 기록되는 곳

Table에는 행에서 고유하게 식별 가능한 기본 키라는 속성이 있으며 외래 키를 사용하여 각 행에서 서로 다른 테이블 간의 관계를 만들 수 있음

데이터는 기본 키 또는 외래 키를 통해 결합(join)될 수 있는 여러 테이블에 걸쳐 구조화됨

### **SQL**
---

![](https://velog.velcdn.com/images/lurelight/post/2234995c-fac1-4074-bdd2-ee558eb535cc/image.png)

**SQL (Structure Query Language)**

데이터베이스에 정보를 저장하고 처리하기 위한 프로그래밍 언어

![](https://velog.velcdn.com/images/lurelight/post/36dc2066-7b88-4bba-a392-376b4f6d4939/image.png)

**SQL Syntax**

1. SQL 키워드는 대소문자를 구분하지 않음

- 하지만 대문자로 작성하는 것을 권장 (명시적 구분)

2. 각 SQL Statements의 끝에는 세미콜론 (;)이 필요

- 세미콜론은 각 SQL Statements을 구분하는 방법 (명령어의 마침표)

![](https://velog.velcdn.com/images/lurelight/post/0df9d564-5fe6-400d-9dea-027430a71dca/image.png)

### **SQL Statements**
---

**SQL Statements**

SQL을 구성하는 가장 기본적인 코드 블록

**SQL Statements 예시**

해당 예시 코드는 SELECT Statement라 부름

이 Statement 는 SELECT, FROM 2개의 keyword로 구성됨

![](https://velog.velcdn.com/images/lurelight/post/4e6e611c-3468-44db-b788-8625bf0db452/image.png)

**수행 목적에 따른 SQL Statements 4가지 유형**

1. DDL - 데이터 정의

2. DQL - 데이터 검색

3. DML - 데이터 조작

4. DCL - 데이터 제어

![](https://velog.velcdn.com/images/lurelight/post/714528a2-f921-44a8-8420-beb3e983caa5/image.png)

**SQL 학습 방향**

단순히 SQL 문법을 암기하고 상황에 따라 실행하는 것이 아닌 SQL을 통해 관계형 데이터베이스를 잘 이해하고 다루는 방법을 학습

**참고**
---

**Query**

데이터베이스로부터 정보를 요청하는 것

일반적으로 SQL로 작성하는 코드를 쿼리문(SQL 문)이라고 한다.

**SQL 표준**

SQL은 미국 국립 표준 협회 (ANSI)와 국제 표준화 기구(ISO)에 의해 표준이 채택됨

모든 RDBMS에서 SQL 표준을 지원

다만 각 RDBMS마다 독자적인 기능에 따라 표준을 벗어나는 문법이 존재하니 주의

### **Single Table Queries**
---

데이터를 조회하는 유형은 DQL 밖에 없음

![](https://velog.velcdn.com/images/lurelight/post/9371da55-469f-4d7d-8292-571a17ab5149/image.png)

### **Querying data**
---

**SELECT**

테이블에서 데이터를 조회

SELECT 키워드 이후 데이터를 선택하려는 필드를 하나 이상 지정

FROM 키워드 이후 데이터를 선택하려는 테이블의 이름을 지정

![](https://velog.velcdn.com/images/lurelight/post/d91aebc2-7755-433d-815c-e5b99195dd77/image.png)

![](https://velog.velcdn.com/images/lurelight/post/35111f59-11c6-4935-a8ee-0c34589873ed/image.png)

![](https://velog.velcdn.com/images/lurelight/post/6bd79fd1-8265-4a0f-a755-6c02c8739526/image.png)

![](https://velog.velcdn.com/images/lurelight/post/1f38e98f-bede-45e2-8fd2-28b3109ab415/image.png)

![](https://velog.velcdn.com/images/lurelight/post/a139a15d-3ca7-45bc-b26e-4225c6e03795/image.png)

![](https://velog.velcdn.com/images/lurelight/post/129316f5-7c98-4d6d-b489-681779dda10b/image.png)

![](https://velog.velcdn.com/images/lurelight/post/4dd651bf-7b85-4911-9061-6a8b99294f9f/image.png)

![](https://velog.velcdn.com/images/lurelight/post/8fa6b81e-c0a5-4899-8313-8585d23d2b8c/image.png)

![](https://velog.velcdn.com/images/lurelight/post/ad810373-a71b-4587-a7c2-0e2462a20123/image.png)

![](https://velog.velcdn.com/images/lurelight/post/f013eb75-d637-4283-8b18-9ff2919cc3d2/image.png)

**SELECT 정리**

테이블의 데이터를 조회 및 반환

'*' (asterisk)를 사용하여 모든 필드를 선택

### **Sorting Data**
---

**ORDER BY**

조회 결과의 레코드를 정렬

![](https://velog.velcdn.com/images/lurelight/post/31a8c1e1-447c-465e-bb6a-7c9d7566510f/image.png)

![](https://velog.velcdn.com/images/lurelight/post/183381ee-c835-4d70-9bbf-245b46901c32/image.png)

```
SELECT FirstName FROM employees ORDER BY FirstName;
```

![](https://velog.velcdn.com/images/lurelight/post/c41eb2f7-362e-42c8-83c8-6e3f0875c32d/image.png)

```
SELECT FirstName FROM employees ORDER BY FirstName DESC;
```

![](https://velog.velcdn.com/images/lurelight/post/e2026ad8-37fb-4920-bb9e-f73d94afd5fd/image.png)

```
SELECT Country, City FROM customers ORDER BY Country DESC, City;
```

![](https://velog.velcdn.com/images/lurelight/post/af537a6e-895e-4bb5-9f78-67b4f6145cd0/image.png)

```
SELECT Name, Milliseconds/60000 AS '재생 시간(분)' FROM tracks ORDER BY Milliseconds DESC;
```

![](https://velog.velcdn.com/images/lurelight/post/fac3e1f8-bec9-4590-a008-6b5e8d8c57e9/image.png)

```
SELECT ReportsTo FROM employees ORDER BY ReportsTo;
```

![](https://velog.velcdn.com/images/lurelight/post/db9f1ee0-1aa7-438b-b156-16cca1f86771/image.png)

### **Filtering Data**
---

![](https://velog.velcdn.com/images/lurelight/post/06f8ca75-4a8d-49d5-8625-1f2549fe01c5/image.png)

**DISTINCT**

조회 결과에서 중복된 레코드를 제거

![](https://velog.velcdn.com/images/lurelight/post/69742aff-f8d0-401e-a465-6402fb021c6a/image.png)

![](https://velog.velcdn.com/images/lurelight/post/2b06cc67-663b-4612-8665-e71adb4fce6f/image.png)

```
SELECT DISTINCT Country FROM customers ORDER BY Country;
```

**WHERE**

조회 시 특정 검색 조건을 지정

![](https://velog.velcdn.com/images/lurelight/post/8d1ba447-9906-44a1-b64f-e37a07986aa9/image.png)

![](https://velog.velcdn.com/images/lurelight/post/99e67840-268a-4d0f-920f-3d3cb32f6f5c/image.png)

```
SELECT LastName, FirstName, City FROM customers WHERE City = 'Prague';
```

![](https://velog.velcdn.com/images/lurelight/post/b139a1dc-ebf8-42a9-bcc8-e32439a128c9/image.png)

```
SELECT LastName, FirstName,City FROM customers WHERE City != 'Prague';
```

![](https://velog.velcdn.com/images/lurelight/post/38d7782d-2faf-4b96-9acc-f97138216a16/image.png)

```
SELECT LastName, FirstName, Company, Country FROM customers WHERE Company IS NULL AND Country = 'USA';
```

![](https://velog.velcdn.com/images/lurelight/post/edc2487d-b462-4479-a4d3-8fba08105331/image.png)

```
SELECT LastName, FirstName, Company, Country FROM customers WHERE Company IS NULL OR Country = 'USA';
```

![](https://velog.velcdn.com/images/lurelight/post/8f9b3ef1-62ec-432e-ada8-0500c077c140/image.png)

```
SELECT Name, Bytes FROM tracks WHERE 100000 <= Bytes AND Bytes <= 500000;
```

```
SELECT Name, Bytes FROM tracks WHERE Bytes BETWEEN 100000 AND 500000;
```

![](https://velog.velcdn.com/images/lurelight/post/bf82c0c6-3a44-456d-812a-4ab8cd8e62bf/image.png)

```
SELECT Name, Bytes FROM tracks WHERE Bytes BETWEEN 100000 AND 500000 ORDER BY Bytes;
```

![](https://velog.velcdn.com/images/lurelight/post/11476ced-1997-474c-a294-626cf21b3c43/image.png)

```
SELECT LastName, FirstName, Country FROM customers WHERE Country = 'Canada' OR Country = 'Germany' OR Country = 'France';
```

![](https://velog.velcdn.com/images/lurelight/post/5d07377e-d75d-4fa6-b8d7-5db8f0f945ae/image.png)

```
SELECT LastName, FirstName, Country FROM customers WHERE Country IN ('Canada', 'Germany', 'France');
```

```
SELECT LastName, FirstName, Country FROM customers WHERE Country NOT IN ('Canada', 'Germany', 'France');
```

![](https://velog.velcdn.com/images/lurelight/post/43a29e7a-2ee3-4517-aea2-fc536314e177/image.png)

```
SELECT LastName, FirstName FROM customers WHERE LastName LIKE '%son';
```

![](https://velog.velcdn.com/images/lurelight/post/35ff9c6d-e76b-4bee-ba65-8f0c8da8c5a9/image.png)

```
SELECT LastName, FirstName FROM customers WHERE FirstName LIKE '___a';
```

**Operators**

Comparison Operators (비교 연산자)

=, >=, <=, !=, IS, LIKE, IN, BETWEEN ...AND

Logical Operators (논리 연산자)

AND, OR, NOT

**IN Operator**

값이 특정 목록 안에 있는지 확인

**LIKE Operator**

값이 특정 패턴에 일치하는지 확인 (Wildcards와 함께 사용)

**Wildcard Characters**

'%' 문자열과 일치하는지 확인

'_' 단일 문자와 일치하는지 확인

**LIMIT**

LIMIT clause

조회하는 레코드 수를 제한

![](https://velog.velcdn.com/images/lurelight/post/79f0e520-8a5f-4288-843b-9b515138d3b4/image.png)

![](https://velog.velcdn.com/images/lurelight/post/9c99b297-4f38-4c1f-9b2a-009bf8ad8691/image.png)

![](https://velog.velcdn.com/images/lurelight/post/7f121a5e-1964-42c8-bab6-a41194b8fbb7/image.png)

```
SELECT TrackId, Name, Bytes FROM tracks ORDER BY Bytes DESC LIMIT 7;
```

![](https://velog.velcdn.com/images/lurelight/post/a5f423bb-5544-4b9b-999f-c52c9ee7c93c/image.png)

```
SELECT TrackId, Name, Bytes FROM tracks ORDER BY Bytes DESC LIMIT 3, 4;
```

### **Grouping data**
---

**GROUP BY**

레코드를 그룹화하여 요약본 생성 ('집계 함수'와 함께 사용)

**Aggregation Functions (집계 함수)**

값에 대한 계산을 수행하고 단일한 값을 반환하는 함수

SUM, AVG, MAX, MIN, COUNT

![](https://velog.velcdn.com/images/lurelight/post/07aba51f-09e6-43d1-acc4-2259486b3b8f/image.png)

![](https://velog.velcdn.com/images/lurelight/post/1c05497c-b87e-475c-a69c-cfec286e0bf7/image.png)

![](https://velog.velcdn.com/images/lurelight/post/e18561bd-d48d-446c-86d2-70136e35adb5/image.png)

```
SELECT Country FROM customers GROUP BY Country;
```

![](https://velog.velcdn.com/images/lurelight/post/c31399e8-1b54-4885-a9aa-facb53431aca/image.png)

```
SELECT Composer, AVG(Bytes) FROM tracks GROUP BY Composer ORDER BY AVG(Bytes) DESC;
```

![](https://velog.velcdn.com/images/lurelight/post/11b1de77-2726-4fff-8b2b-f320b1e308dc/image.png)

```
SELECT Composer, AVG(Milliseconds/60000) FROM tracks GROUP BY Composer HAVING AVG(Milliseconds/60000) < 10 ;
```

![](https://velog.velcdn.com/images/lurelight/post/ce229195-17f5-426c-94a3-54745cf46918/image.png)

![](https://velog.velcdn.com/images/lurelight/post/290b419f-ae46-418e-9e44-f18510d36e29/image.png)

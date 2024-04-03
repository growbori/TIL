# 외래키(Foreign key)
- 의존성을 생성한다.

## 예시 코드
- 외래키 == 제약조건 -> 
    - 참조하는 테이블에 미리 생성된 행을 반드시 참조해야 한다.
    - 참조하는 외래키 값이 반드시 존재해야 하는 제약이 따른다.
- users 테이블

```sql
CREATE TABLE Users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(30) NOT NULL,
);
```
- 주문 테이블
```sql
CREATE TABLE Orders(
    OrderId INTEGER PRIMARY KEY AUTOINCREMENT,
    OrderDate DATE NOT NULL,
    UserId INTEGER,
    FOREIGN KEY (UserId) REFERENCES Users(id)
);

```
논리적 참조 관계인 무결성도 동시에 가져올 수 있다.

- 참조 무결성




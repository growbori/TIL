### **상속**
---

개요

**상속 (Inheritance)**
기존 클래스의 속성과 메서드를 물려받아 새로운 하위 클래스를 생성하는 것

**상속이 필요한 이유**

1. 코드 재사용

    - 상속을 통해 기존 클래스의 속성과 메서드를 재사용할 수 있음
    
    - 새로운 클래스를 작성할 때 기존 클래스의 기능을 그대로 활용할 수 있으며, 중복된 코드를 줄일 수 있음
    
2. 계층 구조

    - 상속을 통해 클래스들 간의 계층 구조를 형성할 수 있음
    
    - 부모 클래스와 자식 클래스 간의 관계를 표현하고, 더 구체적인 클래스를 만들 수 있음
    
3. 유지 보수의 용이성

    - 상속을 통해 기존 클래스의 수정이 필요한 경우, 해당 클래스만 수정하면 되므로 유지 보수가 용이해짐 
    
    - 코드의 일관성을 유지하고, 수정이 필요한 범위를 최소화할 수 있음

![image](https://github.com/ragu6963/TIL/assets/32388270/f259eed5-c629-4a42-b0cc-4896162169c8)

### **클래스 상속**
---

**상속 없이 구현 하는 경우 (1/2)**

- 학생/교수 정보를 나타내기 어려움

![](https://velog.velcdn.com/images/lurelight/post/c9b43a0b-29e5-4f26-9c1f-00e4cb20f068/image.png)

**상속 없이 구현 하는 경우 (2/2)**

- 메서드 중복 정의

![](https://velog.velcdn.com/images/lurelight/post/27fed557-f160-475f-ad20-df897fb99ae7/image.png)

![](https://velog.velcdn.com/images/lurelight/post/d24745eb-2b06-480e-863b-e2e15382d3db/image.png)

**super()**

- 부모 클래스 객체를 반환하는 내장 함수

![](https://velog.velcdn.com/images/lurelight/post/b5aa2309-046f-495d-8ad4-d1496c4d56e6/image.png)

### **다중 상속**
---

**다중 상속**

다중 상속 정의

- 둘 이상의 상위 클래스로부터 여러 행동이나 특징을 상속받을 수 있는 것

- 상속받은 모든 클래스의 요소를 활용 가능함

- 중복된 속성이나 메서드가 있는 경우 <span style='color:crimson;'>상속 순서에 의해 결정</span>됨

![](https://velog.velcdn.com/images/lurelight/post/40a87e9f-4fde-4a18-b4d2-25a5d39cc36b/image.png)

![](https://velog.velcdn.com/images/lurelight/post/5d5fef8d-2f2f-4b3e-8481-0f13d6f3c6b2/image.png)

중복된 속성이나 매서드가 있는 경우 상속 순서대로 결정된다!

![](https://velog.velcdn.com/images/lurelight/post/5fb948e5-abc2-4874-bae9-074fc44a2d81/image.png)

**파이썬에서의 해결책**

- MRO(Method Resolution Order) 알고리즘을 사용하여 클래스 목록을 생성

- 부모 클래스로부터 상속된 속성들의 검색을 깊이 우선으로, **왼쪽에서 오른쪽으로**, 계층 구조에서 겹치는 같은 클래스를 두 번 검색하지 않음

- 그래서, 속성이 D 에서 발견되지 않으면, B 에서 찾고, 거기에서도 발견되지 않으면, C 에서 찾고, 이런 식으로 진행됨

![](https://velog.velcdn.com/images/lurelight/post/15327f99-9a83-4cf6-ae1f-75138722b2f3/image.png)

**MRO (Method Resolution Order)**

- 메서드 결정 순서

**super()**

- 부모 클래스 객체를 반환하는 내장 함수

- 다중 상속 시 MRO를 기반으로 현재 클래스가 상속하는 모든 부모 클래스 중 다음에 호출될 메서드를 결정하여 자동으로 호출

![](https://velog.velcdn.com/images/lurelight/post/1b6b580a-85e8-4f3b-ad6e-bb72210d1f32/image.png)

![](https://velog.velcdn.com/images/lurelight/post/3ae5fc28-10e9-494d-9e3e-9f29cc634d25/image.png)

![](https://velog.velcdn.com/images/lurelight/post/52b73a85-6db0-4a10-a257-22d178608ab9/image.png)

![](https://velog.velcdn.com/images/lurelight/post/6433effe-9dc4-433c-913a-5c6880637e18/image.png)

**mro() 메서드**

- 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드

- 기존의 인스턴스 -> 클래스 순으로 이름 공간을 탐색하는 과정에서 상속 관계에 있으면 인스턴스 -> 자식 클래스 -> 부모 클래스로 확장

**super의 2 가지 사용 사례**

1. 단일 상속 구조

    - 명시적으로 이름을 지정하지 않고 부모 클래스를 참조할 수 있으므로, 코드를 더 유지 관리하기 쉽게 만들 수 있음
    
    - 클래스 이름이 변경되거나 부모 클래스가 교체되어도 super()를 사용하면 코드 수정이 더 적게 필요
    
2. 다중 상속 구조

    - MRO를 따른 메서드 호출
    
    - 복잡한 다중 상속 구조에서 발생할 수 있는 문제를 방지

MRO 가 필요한 이유

- 부모 클래스들이 여러 번 액세스 되지 않도록, 각 클래스에서 지정된 왼쪽에서 오른쪽으로 가는 순서를 보존하고, 각 부모를 오직 한 번만 출력하고, 부모들의 우선순위에 영향을 주지 않으면서 서브 클래스를 만드는 단조적인 구조 형성

- 프로그래밍 언어의 신뢰성 있고 확장성 있는 클래스를 설계할 수 있도록 도움

- 클래스 간의 메서드 호출 순서가 예측 가능하게 유지되며, 코드의 재사용성과 유지보수성이 향상

### **에러와 예외**
---

디버깅

버그 (bug)

소프트웨어에서 발생하는 오류 또는 결함 프로그램의 예상된 동작과 실제 동작 사이의 불일치

버그의 기원

- 최초의 버그는 1945년 프로그래밍 언어의 일종인 코볼 발명자 그레이스 호퍼가 발견

- 역사상 최초의 버그는 mark 2 라는 컴퓨터 회로에 벌레인 나방이 들어가 합선을 일으켜 비정상적으로 동작한 것을 기록한 것

- 버그라는 용어는 이전부터 사용되어 왔지만 이 사건을 계기로 컴퓨터 시스템에서 발생하는 오류 또는 결함을 지칭하는 용어로 널리 사용되기 시작

**디버깅 (Debugging)**

소프트웨어에서 발생하는 버그를 찾아내고 수정하는 과정

프로그램의 오작동 원인을 식별하여 수정하는 작업

**디버깅 방법**

1. print 함수 활용

    - 특정 함수 결과, 반복/조건 결과 등 나눠서 생각, 코드를 bisection으로 나눠서 생각
    
2. 개발 환경(text editor, IDE) 등에서 제공하는 기능 활용

    - breakpoint, 변수 조회 등
    
3. [Python tutor](https://pythontutor.com/) 활용 (단순 파이썬 코드인 경우) 

4. 뇌 컴파일, 눈 디버깅 등


**에러 (Error)**

프로그램 실행 중에 발생하는 예외 상황

**파이썬의 에러 유형**

- 문법 에러 (Syntax Error)

    - 프로그램의 구문이 올바르지 않은 경우 발생 (오타, 괄호 및 콜론 누락 등의 문법적 오류)
    
- 예외 (Exception)

    - 프로그램 실행 중에 감지되는 에러

![](https://velog.velcdn.com/images/lurelight/post/0e8747e5-891f-4317-a65e-3e0f7f181381/image.png)

![](https://velog.velcdn.com/images/lurelight/post/32695f9d-8170-4eb4-92c9-f1f5049affbc/image.png)

### **예외**
---

**예외 (Exception)**

프로그램 실행 중에 감지되는 에러

**내장 예외 (Built-in Exceptions)**

- 예외 상황을 나타내는 예외 클래스들

- 파이썬에서 이미 정의되어 있으며, 특정 예외 상황에 대한 처리를 위해 사용

> 참고 문서 : https://docs.python.org/ko/3/library/exceptions.html#ValueError

![](https://velog.velcdn.com/images/lurelight/post/49d0dc3f-0a3b-43dd-a72e-34195d687062/image.png)

![](https://velog.velcdn.com/images/lurelight/post/85193545-6f6d-4afa-9d34-63e5ad3c9051/image.png)

![](https://velog.velcdn.com/images/lurelight/post/12bca978-e91e-4560-87d9-d833fccc6210/image.png)

![](https://velog.velcdn.com/images/lurelight/post/87529ddb-20dc-4f32-a2c3-d117d0fb3b48/image.png)

![](https://velog.velcdn.com/images/lurelight/post/7e49197d-9fe1-4ddf-b02e-d50e41be72ef/image.png)

![](https://velog.velcdn.com/images/lurelight/post/5e47e51b-8ef8-42e1-8fa4-4b9e4b8db8f8/image.png)

![](https://velog.velcdn.com/images/lurelight/post/a85a6456-f839-4ad7-9ae9-8c604649dd93/image.png)

![](https://velog.velcdn.com/images/lurelight/post/bb3821e8-2e0d-4ca6-93e7-0d63629568b5/image.png)

![](https://velog.velcdn.com/images/lurelight/post/05f5663c-2b2d-4b2d-9eae-406d776833a6/image.png)

![](https://velog.velcdn.com/images/lurelight/post/7496b383-9863-4908-a2bb-72ad5bdaa401/image.png)

### **예외 처리**
---

**try 와 except**

파이썬에서는 <span style='color:red;'>try</span> 문과 <span style='color:red;'>except</span> 절을 사용하여 예외 처리

**try-except 구조**

- try 블록 안에는 예외가 발생할 수 있는 코드를 작성

- except 블록 안에는 예외가 발생했을 때 처리할 코드를 작성

- 예외가 발생하면 프로그램 흐름은 try 블록을 빠져나와 해당 예외에 대응하는 except 블록으로 이동

**Base Exception**

모든 예외 상황들을 아우르는 예외들의 Class

![](https://velog.velcdn.com/images/lurelight/post/c4ad3608-c975-44d2-bb96-3cf6cb0c6cf0/image.png)

![](https://velog.velcdn.com/images/lurelight/post/acade92b-d28a-4487-89fd-aadaca2e4ce2/image.png)

![](https://velog.velcdn.com/images/lurelight/post/2f2dfba1-26ff-4df6-b10e-fead0f459cd3/image.png)

![](https://velog.velcdn.com/images/lurelight/post/904ad8fc-1a7f-4d67-8fdf-ce1ed16df239/image.png)

![](https://velog.velcdn.com/images/lurelight/post/227b810d-ee4a-494d-b735-a030f4d3e36d/image.png)

![](https://velog.velcdn.com/images/lurelight/post/3d422d41-09fb-4c9e-966c-89f663e0abaf/image.png)

![](https://velog.velcdn.com/images/lurelight/post/4c236b39-4c39-4dba-8e0d-081c0873f0b7/image.png)

![](https://velog.velcdn.com/images/lurelight/post/1e4383bc-b094-43a1-9d1a-9097b4e46b5b/image.png)

### **참고**
---

**as 키워드**

- as 키워드를 활용하여 에러 메시지를 except 블록에서 사용할 수 있음

![](https://velog.velcdn.com/images/lurelight/post/5fa0bbea-c87e-43f9-97b9-7411fdcd4590/image.png)


### **EAFP & LBYL**
---

개요

**예외처리와 값 검사에 대한 2가지 접근 방식**

1. EAFP

2. LBYL

**EAFP (“Easier to Ask for Forgiveness than Permission”)**

예외처리를 중심으로 코드를 작성하는 접근 방식 (try-except)

**LBYL (“Look Before You Leap”)**

값 검사를 중심으로 코드를 작성하는 접근 방식 (if-else)

![](https://velog.velcdn.com/images/lurelight/post/5f2a0816-8b27-4fe8-9774-3e2cb6a9234b/image.png)

![](https://velog.velcdn.com/images/lurelight/post/c21d0c21-c065-4319-9849-c13b78db7375/image.png)




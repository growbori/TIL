### **Tree**
---

#### **트리, 높이 시험에 나옴 중요!**

**트리**

비선형 구조

원소들 간에 1 : n 관계를 가지는 자료 구조

원소들 간에 계층 관계를 가지는 계층형 자료구조

상위 원소에서 하위 원소로 내려가면서 확장되는 트리(나무)모양의 구조

한개 이상의 노드로 이루어진 유한집합이며 다음 조건을 만족한다.

- 노드 중 최상위 노드를 루트(root)라 한다.

- 나머지 노드들은 n(>=0)개의 분리 집합 T1, ..., TN으로 분리될 수 있다.

이들 T1, ...., TN은 각각 하나의 트리가 되며 (재귀적 정의) 루트의 부 트리(subtree)라 한다.

![](https://velog.velcdn.com/images/lurelight/post/dfd536eb-ef5b-4cee-887a-d00e34ae8b3a/image.png)

노드(node) - 트리의 원소

- 트리 T의 노드 - A, B, C, D, E, F, G, H, I, J, K

간선(edge) - 노드를 연결하는 선. 부모 노드와 자식 노드를 연결

루트 노드 (root node) - 트리의 시작 노드

- 트리 T의 루트노드 -A

![](https://velog.velcdn.com/images/lurelight/post/766ac117-315b-46c0-8a95-5515aecbabb4/image.png)

형제 노드(sibling node) - 같은 부모 노드의 자식 노드들

- B, C, D는 형제 노드

조상 노드 - 간선을 따라 루트 노드까지 이르는 경로에 있는 모든 노드들

- K의 조상 노드 : F, B, A

서브 트리 (subtree) : 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리

자손 노드 - 서브 트리에 있는 하위 레벨의 노드들

- B의 자손 노드 : E, F, K

![](https://velog.velcdn.com/images/lurelight/post/81244a5d-3560-4614-b903-6c33c178f1d8/image.png)

**차수 (degree)**

노드의 차수 : 노드에 연결된 자식노드의 수

- B의 차수 = 2, C의 차수 = 1

트리의 차수 : 트리에 있는 노드의 차수 중에서 가장 큰 값

- 트리 T의 차수 = 3

단말 노드 (리프 노드): 차수가 0인 노드, 자식 노드가 없는 노드

B의 자식 노드 : E, F

B의 자손 노드 : E, F, K

높이

노드의 높이 : 루트에서 노드에 이르는 간선의 수. 노드의 레벨

- B의 높이 = 1, F의 높이 = 2

트리의 높이 : 트리에 있는 노드의 높이 중에서 가장 큰 값, 최대 레벨

- 트리T의 높이 = 3

![](https://velog.velcdn.com/images/lurelight/post/42466d4a-ba13-44a9-80c4-0c5de77f31c7/image.png)

높이는 상대적인 개념 자료마다 레벨 0을 높이 0으로 시작할 수도 있고 높이 1로 시작할 수도 있음

### **이진 트리**
---

**이진 트리**

모든 노드들이 2개의 서브 트리를 갖는 특별한 형태의 트리

<span style='color:red;'>**각 노드가 자식 노드를 최대한 2개 까지만 가질 수 있는 트리**</span>

- 왼쪽 자식 노드 (left child node)

- 오른쪽 자식 노드 (right child node)

이진 트리의 예

![](https://velog.velcdn.com/images/lurelight/post/a99d4fbb-68c0-4eb7-a972-c2cbd06ded66/image.png)

**이진 트리의 특성**

![](https://velog.velcdn.com/images/lurelight/post/bb652c73-0b78-46fb-aa06-513c0625adba/image.png)

**이진 트리의 종류**

**포화 이진 트리 (Full Binary Tree)**

모든 레벨에 노드가 포화상태로 차 있는 이진 트리

높이가 h 일때 최대의 노드 개수인 (2^(h+1)- 1) 의 노드를 가진 이진 트리

- 높이가 3일때 2^(3+1)-1 = 15개의 노드

루트를 1번으로 하여 2^(h + 1) -1 까지 정해진 위치에 대한 노드 번호를 가짐

![](https://velog.velcdn.com/images/lurelight/post/3645520e-c945-4749-9762-b10853b770d2/image.png)

**완전 이진 트리 (Complete Binary Tree)**

높이가 h 이고 노드 수가 n개일 때 (단 2^h <= n <= 2^(h+1)-1), 포화 이진 트리의 노드 번호 1번부터 n번까지 빈자리가 없는 이진 트리

예 ) 노드가 10개인 완전 이진 트리

![](https://velog.velcdn.com/images/lurelight/post/2ebef58a-9388-4342-8df5-946654a7c9b0/image.png)

**편향 이진 트리 (Skewed Binary Tree)**

높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드만을 가진 이진 트리

- 왼쪽 편향 이진 트리

- 오른쪽 편향 이진 트리

![](https://velog.velcdn.com/images/lurelight/post/8e60115e-8c69-454c-8f7f-5427400ca4ad/image.png)

### **순회**
---

**순회(traversal)**

순회(traversal)란 트리의 각 노드를 중복되지 않게 전부 방문하는 것을 말하는데 트리는 비선형 구조이기 때문에 선형 구조에서와 같이 선후 연결 관계를 알 수 없다.

따라서 특별한 방법이 필요하다.

트리의 노드들을 체계적으로 방문하는 것

**3가지 기본적인 순회 방법**

전위 순회(predorder traversal) : VLR

- 부모 노드 방문 후, 자식 노드를 좌, 우 순서로 방문한다.

중위 순회 (inorder traversal) : LVR

- 왼쪽 자식 노드, 부모 노드, 오른쪽 자식 노드 순으로 방문한다.

후위 순회(postorder traversal) : LRV

- 자식 노드를 좌우 순서로 방문 후, 부모 노드로 방문한다.

![](https://velog.velcdn.com/images/lurelight/post/e7692caf-2d43-4957-8533-4d796c493ef1/image.png)

**전위 순회 (predorder traversal)**

1) 현재 노드 n을 방문하여 처리한다 -> V

2) 현재 노드 n을 왼쪽 서브트리로 이동한다. -> L

3) 현재 노드 n의 오른쪽 서브트리로 이동한다. -> R

전위 순회 알고리즘

![](https://velog.velcdn.com/images/lurelight/post/2e1ae13b-2ed1-41aa-b04f-bd602572e2cc/image.png)

![](https://velog.velcdn.com/images/lurelight/post/634cc670-47cf-4a42-8353-2776fde1a5f2/image.png)

**중위 순회 (inorder traversal)**

수행 방법

1) 현재 노드 n의 왼쪽 서브 트리로 이동한다 : L

2) 현재 노드 n을 방문하여 처리한다 : V

3) 현재 노드 n의 오른쪽 서브 트리로 이동한다 : R

![](https://velog.velcdn.com/images/lurelight/post/6969d215-dbff-4af7-bcab-07f35fb20409/image.png)

![](https://velog.velcdn.com/images/lurelight/post/fcdb5fb9-76de-4450-9a4e-7bccef260615/image.png)

**후위 순회(postorder traversal)**

루트가 가장 마지막에 처리됨

수행 방법

1) 현재 노드 n의 왼쪽 서브 트리로 이동한다 : L

2) 현재 노드 n의 오른쪽 서브 트리로 이동한다 : R

3) 현재 노드 n을 방문하여 처리한다 : V

![](https://velog.velcdn.com/images/lurelight/post/ed943f0f-42e4-4c52-a0bb-552a1635e88d/image.png)

![](https://velog.velcdn.com/images/lurelight/post/d74a4371-a37f-49eb-8c45-e8c764d82a43/image.png)

![](https://velog.velcdn.com/images/lurelight/post/f4372508-e312-4c0b-bf34-f1307dc0b31d/image.png)

### **이진 트리의 표현**
---

**배열을 이용한 이진 트리의 표현**

이진 트리에 각 노드 번호를 다음과 같이 부여

루트의 번호를 1로 함

레벨 n에 있는 노드에 대하여 왼쪽부터 오른쪽으로 2^n 부터 2^(n+1)-1까지 번호를 차례로 부여

![](https://velog.velcdn.com/images/lurelight/post/bf842cc2-401d-4367-9d26-eeb8ea01f269/image.png)

![](https://velog.velcdn.com/images/lurelight/post/cdf333f5-8ed4-426b-a690-7d05d3ef1688/image.png)

노드 번호가 i인 노드의 부모 노드 번호 : i // 2

![](https://velog.velcdn.com/images/lurelight/post/5be47f38-a3d2-4d40-beec-b716d214981e/image.png)

![](https://velog.velcdn.com/images/lurelight/post/622edcdc-f4ce-46af-b88a-bb220b7a66ce/image.png)

![](https://velog.velcdn.com/images/lurelight/post/554a67f2-e131-4701-b8f6-6c45eccf0e44/image.png)

![](https://velog.velcdn.com/images/lurelight/post/e17316a6-72fc-4ee9-acab-bbcd4e2ec78c/image.png)

![](https://velog.velcdn.com/images/lurelight/post/62578b1e-954b-419c-b8fb-384c97c9d730/image.png)

**배열을 이용한 이진 트리 표현의 단점**

- 편향 이진 트리의 경우에 사용하지 않는 배열 원소에 대한 메모리 공간 낭비 발생

- 트리의 중간에 새로운 노드를 삽입하거나 기존의 노드를 삭제할 경우 배열의 크기 변경 어려워 비효율적

배열을 이용한 이진 트리의 표현의 단점을 보완하기 위해 연결리스트를 이용하여 트리를 표현할 수 있다.

연결 자료구조를 이용한 이진트리의 표현

- 이진 트리의 모든 노드는 최대 2개의 자식 노드를 가지므로 일정한 구조의 단순 연결 리스트 노드를 사용하여 구현

![](https://velog.velcdn.com/images/lurelight/post/6ab9fcdc-35f5-4b17-99a4-dda8d25d985a/image.png)

![](https://velog.velcdn.com/images/lurelight/post/3705d167-a67f-4fb6-b1dd-c8296b9b9fa9/image.png)

**연습문제**

![](https://velog.velcdn.com/images/lurelight/post/c175d94d-01a7-4042-9227-01a204766933/image.png)

```
'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

def pre_order(T):
    if T :
        print(T, end = ' ')
        pre_order(left[T])
        pre_order(right[T])

N = int(input())    #1번부터 N번까지의 정점
E = N-1
arr = list(map(int, input().split()))
left = [0] * (N+1)      # 부모를 인덱스로 왼쪽 자식 번호 저장
right = [0] * (N+1)     # 부모를 인덱스로 오른쪽 자식 번호 저장
par = [0] * (N+1)       # 자식을 인덱스로 부모 저장

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
# for i in range(0, E*2, 2):
#     p, c = arr[i]. arr[i+1]
    if left[p] == 0:        # 왼쪽 자식이 없으면
        left[p] = c
    else:
        right[p] = c
    par[c] = p

c = N
while par[c] != 0:      # 부모가 있으면
    c = par[c]          # 부모를 새로운 자식으로 두고

root = c                # 더이상 부모가 없으면 root
print(root)
pre_order(root)

```



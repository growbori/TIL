### **DP**
---

**DP (Dynamic Programming)**

동적 계획(Dynamic Programming) 알고리즘은 그리디 알고리즘과 같이 최적화 문제를 해결하는 알고리즘이다.

동적 계획 알고리즘은 먼저 입력 크기가 작은 부분들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘이다.

**피보나치 수 DP 적용**

- 피보나치수는 부분 문제의 답으로부터 본 문제의 답을 얻을 수 있으므로 최적 부분 구조로 이루어져 있다.

![](https://velog.velcdn.com/images/lurelight/post/c257844b-d43a-4436-9f66-71fce219267b/image.png)

![](https://velog.velcdn.com/images/lurelight/post/38392989-9a57-4369-b507-b26c14d9b277/image.png)

![](https://velog.velcdn.com/images/lurelight/post/a5ee9819-4872-4158-a969-61042a94ff6d/image.png)

**DP의 구현 방식**

- recursive 방식 : fib1()
- iterative 방식 : fib2()

- <span style='color:red;'>memoization을 재귀적 구조에 사용하는 것 보다 반복적 구조로 DP를 구현한 것이 성능 면에서 보다 효율적이다.</span>

- 재귀적 구조는 내부에 시스템 호출 스택을 사용하는 오버헤드가 발생하기 때문이다.

### **DFS**
---

**DFS (깊이 우선 탐색)**

비선형구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요함.

**깊이 우선 탐색 (Depth First Search, DFS)**

- 스택을 사용해서 구현할 수도 있지만 다른 방법을 활용해서도 구현할 수 있음

- 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회 방법 (재귀 함수도 가능했었음)

- 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 후입선출 구조의 스택 사용

- <span style='color:red;'>인접인 것 중에 빠른 순서대로 접근</span>
![](https://velog.velcdn.com/images/lurelight/post/8f716aaf-c398-4a32-b12e-1569e7b81ed2/image.png)

![](https://velog.velcdn.com/images/lurelight/post/fe362564-38a0-49c4-89f8-07417e9fbf1a/image.png)

![](https://velog.velcdn.com/images/lurelight/post/3f8aa71b-8d68-4da9-932e-154a73bd691e/image.png)

![](https://velog.velcdn.com/images/lurelight/post/12dbfae0-34a9-44c9-95e3-1dcbba06df32/image.png)

![](https://velog.velcdn.com/images/lurelight/post/14a3cd52-b8fe-4d5b-b3e9-ad981f2c1349/image.png)

![](https://velog.velcdn.com/images/lurelight/post/6f8ced39-cab5-4946-b2a0-3a459c3a85b6/image.png)

![](https://velog.velcdn.com/images/lurelight/post/e6096902-db9a-465a-8301-4c6eded4894c/image.png)

![](https://velog.velcdn.com/images/lurelight/post/b4ed555d-b650-47d3-8104-51dc250c1b1d/image.png)

![](https://velog.velcdn.com/images/lurelight/post/2f372ff4-d425-493b-8671-83376d46a1f0/image.png)

![](https://velog.velcdn.com/images/lurelight/post/059a3e46-e55c-4b4e-89e7-f45e2cc1caa6/image.png)

![](https://velog.velcdn.com/images/lurelight/post/9e3b51f6-29a5-409e-8733-df3cc2a7d00a/image.png)

![](https://velog.velcdn.com/images/lurelight/post/1779c423-c456-4ce1-88de-83f626114f1b/image.png)

![](https://velog.velcdn.com/images/lurelight/post/a46df1ef-f593-412c-8032-f11a31cffd18/image.png)

![](https://velog.velcdn.com/images/lurelight/post/1fe6e0d3-c104-48aa-83a6-62ef06d854ae/image.png)

![](https://velog.velcdn.com/images/lurelight/post/74821a51-7a53-4006-b4a4-4405ca8beb55/image.png)

![](https://velog.velcdn.com/images/lurelight/post/6a4d3784-90d5-4c6d-8bf0-926da1d5235c/image.png)

![](https://velog.velcdn.com/images/lurelight/post/dece906f-b94b-4a2e-9296-9ab43d04b752/image.png)

![](https://velog.velcdn.com/images/lurelight/post/69645cbf-3c15-4dc2-a882-e8e1451da6a3/image.png)

가장 최근에 갔던 곳 부터 스택으로 꺼내기

시작 정점 번호, 마지막 정점 번호 주어짐 2개 숫자씩 간선으로 이어져있다고 이해하면 됨

```
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def dfs(i, V): # 시작 i, 마지막 V
    visited = [0] * (V+1) # visited, stack 생성 및 초기화
    stack = []
    visited[i] = 1  # 시작점 방문
    print(i)        # 정점에서 할 일
    while True:     # 탐색
        for w in adjl[i] :# 현재 방문한 정점에 인접하고 방문안한 정점w가 있으면
            if visited[w] == 0 : # 만약 방문한 적이 없으면
                stack.append(i) # push(i), i를 지나서
                i = w # w에 방문
                visited[i] = 1 # 방문해서 할일(1표시)
                print(i)
                break # for w
        else:                   # for w, i에 남은 인접 정점이 없으면
            if stack:   # 스택이 비어있지 않으면(지나온 정점이 남아있으면)
                i = stack.pop()
            else:
                break   # while True
    return

V, E = map(int, input().split())
arr =list(map(int, input().split()))

# 인접리스트
adjl = [[] for _ in range(V+1)] # ardjl[i] 행에 i에 인접인 정점번호

for i in range(E):
    n1, n2 = arr[i * 2] , arr[i * 2 + 1]
    adjl[n1].append(n2)
    adjl[n2].append(n1) # 방향이 없는 경우 방향이 있는 경우에는 넣으면 안됨

# print(adjl)
'''
[[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]
0번에 인접한 숫자, 1번에 인접한 숫자, 2번에 인접한 숫자...
'''
dfs(1, V) # 1번부터 탐색하고 마지막 정점 번호는 V

```


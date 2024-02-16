### **BFS**
---

**BFS (Breadth First Search)**

그래프를 탐색하는 방법에는 크게 두 가지가 있음

- 깊이 우선 탐색 (Depth First Search, BFS)

- 너비 우선 탐색 (Breadth First Search, BFS)

너비 우선 탐색은 탐색 시작점의 <span style='color:red;'>인접한 정점들을 먼저 모두 차례로 방문</span>한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식

인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비우선탐색을 진행해야 하므로 <span style='color:red;'>선입선출 형태의 자료구조인 큐를 활용함</span>

![](https://velog.velcdn.com/images/lurelight/post/7dbd45d0-7337-462a-b242-9d1cc5f64f2f/image.png)

출발 노드로 부터의 거리 혹은 시간을 구해야 할 때 사용

![](https://velog.velcdn.com/images/lurelight/post/a1d410f3-aa08-40be-a76a-61397d3ad9ec/image.png)

![](https://velog.velcdn.com/images/lurelight/post/05f18e49-9ba9-4a60-bf20-419312c9eaa1/image.png)

![](https://velog.velcdn.com/images/lurelight/post/2d0803ed-e6c2-4142-b5e7-7f2bed948a1e/image.png)

![](https://velog.velcdn.com/images/lurelight/post/de6c1fc1-8672-4ef4-bba6-784087652efd/image.png)

![](https://velog.velcdn.com/images/lurelight/post/6013496c-3d57-4b1e-90fe-fc25f0a7e60a/image.png)

C에 인접하면서 방문하지 않은 점

A는 인접이지만 이미 방문했기 때문에 제외

![](https://velog.velcdn.com/images/lurelight/post/51da9829-aa1d-4676-b5d3-e6783ca973f7/image.png)

![](https://velog.velcdn.com/images/lurelight/post/5b77f192-14d1-4bda-b3ba-21d3999a2c64/image.png)

![](https://velog.velcdn.com/images/lurelight/post/af2df266-7a25-41f8-8ef1-fd0afd981aec/image.png)

![](https://velog.velcdn.com/images/lurelight/post/5b0e803f-811a-40b9-bed8-3649ca24f532/image.png)

![](https://velog.velcdn.com/images/lurelight/post/afb73eb3-ebba-491f-b97b-30cd000974ed/image.png)

![](https://velog.velcdn.com/images/lurelight/post/44437fbc-11fc-4a0e-95e3-1e016cdc0f61/image.png)

![](https://velog.velcdn.com/images/lurelight/post/98ecaf18-cb39-4824-9b69-0125d8a04f8e/image.png)

### **BFS 예제**
---

![](https://velog.velcdn.com/images/lurelight/post/4d87e87e-ca89-4e21-b5c9-34befe93be30/image.png)

![](https://velog.velcdn.com/images/lurelight/post/a6ef88e7-748d-4e90-aaea-1f48be3e3c03/image.png)

아까랑 다르게 Q에 요소를 넣을 경우 visited 에 방문 표시를 남김

![](https://velog.velcdn.com/images/lurelight/post/74c30e61-ae3e-4bee-8fec-43e85a159b4f/image.png)

가장 빠른 속도로 처리됨 -> 트리 같은 형태

![](https://velog.velcdn.com/images/lurelight/post/31a510c5-6cca-4644-a772-d9651ef97805/image.png)

![](https://velog.velcdn.com/images/lurelight/post/e3ef96d3-9ba0-4699-a724-a7e6e87f3f35/image.png)

거리에 관련된 정보를 구하고자 할 땐 BFS를 쓰는 것이 좋음

```
'''
V E : V 1~V 번 까지 V 개의 정점. E 개의 간선
E개의 간선 정보
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(s, N) :     # 시작정점 s, 노드 개수 N
    q = []  # 큐
    visited = [0] * (N+1)   # visited
    q.append(s)         # 시작점 인큐
    visited[s] = 1      # 시작점 방문표시
    while q:            # 큐가 비워질때까지...(남은 정점이 있으면)
        t = q.pop(0)
        # t에서 할 일....
        print(t)
        for i in adjl[t]:   # t에 인접인 정점
            if visited[i] == 0:     # 방문하지 않은 정점이면
                q.append(i)     # 인큐
                visited[i] = 1 + visited[t]     # 방문표시
    # print(visited)  # 거리 정보를 얻을 수 있음
V, E = map(int, input().split())

arr = list(map(int, input().split()))
# 인접 리스트 형태로 저장
adjl = [[] for _ in range(V+1)] # 0번부터 V 번 까지 배열을 갖는 리스트를 생성
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]   # 2개의 쌍을 읽어내는 방법
    adjl[n1].append(n2)
    adjl[n2].append(n1)     # 무향그래프

bfs(1, V)

```

노드의 거리

```
'''
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6 
7 4
1 6
2 3
2 6
3 5
2 5 
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9
'''
def bfs(s, N, G) :     # 시작정점 s, 노드 개수 N
    q = []  # 큐 생성
    visited = [0] * (N+1)   # visited 생성
    q.append(s)         # 시작점 인큐
    visited[s] = 1      # 인큐 표시
    while q:            # 처리 안된 정점이 남아있으면
        t = q.pop(0)    # 처리할 정점 디큐
        if t == G:
            return  visited[t] - 1    # 시작 점이 1부터 시작하기 때문에 간선 수를 나타내기 위해선 -1을 해줘야 함
        for i in adjl[t]:           # t 의 인접 정점이
            if visited[i]==0:           # 인큐되지 않았으면(처리된 적이 없으면)
                q.append(i)
                visited[i] = visited[t] + 1
    return  0           # G까지 경로가 없는 경우
T = int(input())
for tc in range(T):
    V, E = map(int, input().split())

    # 인접 리스트 형태로 저장
    adjl = [[] for _ in range(V+1)] # 0번부터 V 번 까지 배열을 갖는 리스트를 생성
    for i in range(E):
        n1, n2 = map(int, input().split())   # 2개의 쌍을 읽어내는 방법
        adjl[n1].append(n2)
        adjl[n2].append(n1)     # 무향그래프
    S, G = map(int, input().split())
    print(f'#{tc+1} {bfs(S, V, G)}')    # G 끝까지 가는 목적지



```







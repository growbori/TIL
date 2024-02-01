### **검색(Search)**
---

**검색**

저장되어 있는 자료 중에서 원하는 항목을 찾는 작업

목적하는 탐색 키를 가진 항목을 찾는 것

- 탐색 키 (search key) : 자료를 구별하여 인식할 수 있는 키

검색의 종류

- 순차 검색 (sequential search)

- 이진 검색 (binary search)

- 해쉬 (hash)

**순차 검색 (sequential search)**

일렬로 되어 있는 자료를 순서대로 검색하는 방법

- 가장 간단하고 직관적인 검색 방법

- 배열이나 연결 리스트 등 순차구조로 구현된 자료구조에서 원하는 항목을 찾을 때 유용함

- 알고리즘이 단순하여 구현이 쉽지만, 검색 대상의 수가 많은 경우에는 수행 시간이 급격히 증가하여 비효율적임

2가지 경우

- 정렬되어 있지 않은 경우

- 정렬되어 있는 경우

**if 정렬되어 있지 않은 경우**

검색 과정

- 첫 번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교하며 찾는다.

- 키 값이 동일한 원소를 찾으면 그 원소의 인덱스를 반환한다.

- 자료구조의 마지막에 이를 때까지 검색 대상을 찾지 못하면 검색 실패

![](https://velog.velcdn.com/images/lurelight/post/89f4d468-4e1c-42bb-b7e2-f9acccbb1c87/image.png)

![](https://velog.velcdn.com/images/lurelight/post/fbe42533-5781-48ac-8605-9a9c066da921/image.png)

찾고자 하는 원소의 순서에 따라 비교 횟수가 결정됨

- 첫 번째 원소를 찾을 때는 1번 비교, 두 번째 원소를 찾을 때는 2번 비교

- 정렬되지 않은 자료에서의 순차 검색의 평균 비교 회수

![](https://velog.velcdn.com/images/lurelight/post/505408bb-63ed-47e1-898b-125b8710854f/image.png)

**정렬되어 있는 경우**

검색과정

- 자료가 오름차순으로 정렬된 상태에서 검색을 실시한다고 가정하자

- 자료를 순차적으로 검색하면서 키 값을 비교하여, 원소의 키 값이 검색 대상의 키 값보다 크면 찾는 원소가 없다는 것으로 더 이상 검색하지 않고 검색을 종료한다.

![](https://velog.velcdn.com/images/lurelight/post/24cabaf7-3aef-4a8c-b477-31bae0edfac2/image.png)

![](https://velog.velcdn.com/images/lurelight/post/c44babfa-8d27-4f9a-b990-8c9a141743fe/image.png)

![](https://velog.velcdn.com/images/lurelight/post/16b620f8-ef26-4a05-a1ae-4eb8c80614bb/image.png)

**이진 검색 (Binary Search)**

**전제조건 : 자료가 정렬된 상태이어야 한다. (오름차순)**

자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법

- 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색을 수행함

이진 검색을 하기 위해서는 자료가 정렬된 상태여야 한다.

**검색 과정**

- 자료의 중앙에 있는 원소를 고른다.

- 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.

- 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행하고, 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다.

- 찾고자 하는 값을 찾을 때까지 1~3 과정을 반복한다.

![](https://velog.velcdn.com/images/lurelight/post/2fc15fc5-fba4-4908-8ba1-4f8a9d47f087/image.png)

![](https://velog.velcdn.com/images/lurelight/post/68850cc5-81ef-494b-84dc-caeaf03e255a/image.png)

**구현 **

- 검색 범위의 시작점과 종료점을 이용하여 검색을 반복 수행한다.

- 이진 검색의 경우, 자료에 삽입이나 삭제가 발생했을 때, 배열의 상태를 항상 정렬 상태로 유지하는 추가 작업이 필요하다.

![](https://velog.velcdn.com/images/lurelight/post/ff8fe017-5f6f-4473-a875-d70f2455fde5/image.png)

![](https://velog.velcdn.com/images/lurelight/post/3de05a1c-22cc-4442-a292-73ea5dc5ff30/image.png)

```
def binary_search(arr, N, key): # arr 구하고자 하는 배열, N 구하고자 하는 범위 key 구하고자 하는 값
    start = 0 # 구간 초기화
    end = N-1

    while start <= end: # 검색 구간이 유효하면 반복
        middle = (start + end) // 2 # 중앙 원소 인덱스
        if arr[middle] == key: # 검색 성공
            return middle
        elif arr[middle] > key:# 중앙값이 키보다 크면
            end = middle - 1
        else: # 키보다 작으면
            start = middle + 1
    return -1 %  # 검색 실패
```

### **선택 정렬**
---

**인덱스**

인덱스라는 용어는 Database에서 유래했으며, 테이블에 대한 동작 속도를 높여주는 자료 구조를 일컫는다. Database 분야가 아닌 곳에서는 Look up table 등의 용어를 사용하기도 한다.

인덱스를 저장하는데 필요한 디스크 공간은 보통 데이블을 저장하는데 필요한 디스크 공간보다 작다. 왜냐하면 보통 인덱스는 키-필드만 갖고 있고 테이블의 다른 세부 항목들은 갖고 있지 않기 때문이다.

**배열을 사용한 인덱스**

대량의 데이터를 매번 정렬하면, 프로그램의 반응은 느려질 수 밖에 없다. 이러한 대량 데이터의 성능 저하 문제를 해결하기 위해 배열 인덱스를 사용할 수 있다.

![](https://velog.velcdn.com/images/lurelight/post/6bb9d53a-cc20-46a1-b9dd-03d51c936016/image.png)

![](https://velog.velcdn.com/images/lurelight/post/64ac21b0-bc4f-438d-bbaa-6a13765d1151/image.png)

**선택 정렬(Selection Sort)**

주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식

- 앞서 살펴본 셀렉션 알고리즘을 전체 자료에 적용한 것이다.

**정렬 과정**

- 주어진 리스트 중에서 최소값을 찾는다.

- 그 값을 리스트의 맨 앞에 위치한 값과 교환한다.

- 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복한다.

![](https://velog.velcdn.com/images/lurelight/post/ee17bd3a-f520-4a67-bb36-8a9b2bff9554/image.png)

![](https://velog.velcdn.com/images/lurelight/post/1628cfa2-bddf-48d3-8c48-1428d7e77bbd/image.png)

![](https://velog.velcdn.com/images/lurelight/post/3873bc93-fb28-4685-ab33-e32709e84b38/image.png)

![](https://velog.velcdn.com/images/lurelight/post/319458c9-b2bf-411c-add4-5f2a153fbc33/image.png)

**선택 정렬 알고리즘**

![](https://velog.velcdn.com/images/lurelight/post/a2866189-9adb-42f5-9da7-9a3754426e9f/image.png)

![](https://velog.velcdn.com/images/lurelight/post/3d5d3b79-30de-4c75-a350-025af6cd620c/image.png)

```

def selectionSort(a, N):
    for i in range(N-1): # 주어진 구간의 시작
        minIdx = i  # 맨 앞 원소를 최솟값 위치로 가정
        for j in range(i+1, N): # 실제 최솟값 위치 검색
            if a[minIdx] > a[j]: # 주어진 공간에서 최솟값 구함
                minIdx = j
        a[i], a[minIdx] = a[minIdx], a[i] # 서로 교환
        
```

**셀렉션 알고리즘 (Selection Algorithm)**

저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법을 셀렉션 알고리즘이라 한다.

- 최소값, 최대값 혹은 중간값을 찾는 알고리즘을 의미하기도 한다.

선택 과정

셀렉션은 아래와 같은 과정을 통해 이루어진다.

- 정렬 알고리즘을 이용하여 자료 정렬하기

- 원하는 순서가 있는 원소 가져오기

**K 번째로 작은 원소를 찾는 알고리즘**

- 1번부터 k번째까지 작은 원소를 찾아 배열의 앞쪽으로 이동시키고, 배열의 k 번째를 반환한다.

- k가 비교적 작을 때 유용하며 O(kn)의 수행시간을 필요로 한다.

![](https://velog.velcdn.com/images/lurelight/post/985fd975-f91b-4358-ae28-a2ddd1a34e6c/image.png)

![](https://velog.velcdn.com/images/lurelight/post/0e339314-95f9-41bc-9c7c-d01a3b460eea/image.png)

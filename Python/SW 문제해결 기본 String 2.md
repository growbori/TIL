### **패턴 매칭**
---

패턴 매칭에 사용되는 알고리즘들

**고지식한 패턴 검색 알고리즘**

비효율적이긴 하나 구현할 줄 알아야 함

![](https://velog.velcdn.com/images/lurelight/post/66a56779-2b39-4751-8244-38ea9adc730e/image.png)

![](https://velog.velcdn.com/images/lurelight/post/db8af603-fef1-4ca3-853b-86b728692ae2/image.png)

![](https://velog.velcdn.com/images/lurelight/post/fab2fe86-9230-4725-8f45-abf356f08ac4/image.png)

![](https://velog.velcdn.com/images/lurelight/post/df694c60-591f-4d49-9436-926b4005d6db/image.png)

**고지식한 패턴 검색 알고리즘의 시간 복잡도**

- 최악의 경우 시간 복잡도는 텍스트의 모든 위치에서 패턴을 비교해야 하므로 O(MN)이 됨

- 길이가 10000인 문자열에서 길이 80인 패턴을 찾는다고 할 때, 최악의 경우 약 10000* 80 = 800000 번의 비교가 일어난다.

- 비교 횟수를 줄일 수 있는 방법은 없는가?

```
def f(pat, txt, M, N):
    for i in range(N-M+1): #txt에서 비교 시작 위치
        for j in range(M):
            if txt[i+j] != pat[j]: # 불일치면 다음 시작 위치로
                break
        else:                      # 패턴 매칭에 성공하면
            return 1

    # 모든 위치에서 비교가 끝난 경우
    return 0

T = int(input())

for tc in range(1, T+1):
    pat = input()
    txt = input()
    M = len(pat)
    N = len(txt)

    ans = f(pat, txt, M, N)
    print(f'#{tc} {ans}')
```

**KMP 알고리즘**

- 불일치가 발생한 텍스트 스트링의 앞 부분에 어떤 문자가 있는지를 미리 알고 있으므로, 불일치가 발생한 앞 부분에 대해서 다시 비교하지 않고 매칭을 수행

- 패턴을 전처리하여 배열 next[M]을 구해서 잘못된 시작을 최소화 함

- next[M] :불일치가 발생했을 경우 이동할 다음 위치

- 시간 복잡도 : O(M+N)

![](https://velog.velcdn.com/images/lurelight/post/3ae2719a-c77f-4636-9fee-cbda8cdcaa0f/image.png)

![](https://velog.velcdn.com/images/lurelight/post/85cb1a9f-b1cf-4e26-ac1b-b894184260ec/image.png)

**보이어 -무어 알고리즘**

![](https://velog.velcdn.com/images/lurelight/post/9275392a-2a15-4f25-b332-07c5206d94fa/image.png)

![](https://velog.velcdn.com/images/lurelight/post/6cbdd611-fdec-4936-b51b-890772572f20/image.png)

![](https://velog.velcdn.com/images/lurelight/post/299cc2eb-caf9-4110-8923-5e3d3e6175e7/image.png)

![](https://velog.velcdn.com/images/lurelight/post/3f80017a-ed06-449d-b725-ec76f44f1135/image.png)

![](https://velog.velcdn.com/images/lurelight/post/b3b25f79-9316-4003-8bda-12fc5f3d1089/image.png)

**문자열 암호화**

시저 암호 (Ceaser cipher)

- 줄리어스 시저가 사용했다고 하는 암호이다.

- 시저는 기원전 100년경에 로마에서 활약했던 장군이다.

- 시저 암호에서는 평문에서 사용되고 있는 알파벳을 일정한 문자 수 만큼 [평행이동] 시킴으로써 암호화를 진행한다.

![](https://velog.velcdn.com/images/lurelight/post/fbb19b56-8971-41fe-8ba5-387c8efff6b4/image.png)

![](https://velog.velcdn.com/images/lurelight/post/5c0b9195-2b45-4dc7-8f01-03c1f9b3a4a6/image.png)

![](https://velog.velcdn.com/images/lurelight/post/2a20996a-b864-49c7-bb02-31d22a9e8e73/image.png)

![](https://velog.velcdn.com/images/lurelight/post/87c7d8f5-2ec2-41fc-b86e-c5c9c1db33fd/image.png)

![](https://velog.velcdn.com/images/lurelight/post/c8016d51-7cbb-4c76-a5ff-68c636a409ad/image.png)

![](https://velog.velcdn.com/images/lurelight/post/a43e2e74-7838-4eb7-b71e-c8df8edf76f3/image.png)

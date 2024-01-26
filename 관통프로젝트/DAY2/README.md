### 관통프로젝트 2 (Netflix)
---
![](https://velog.velcdn.com/images/lurelight/post/aec956ab-a13d-468d-8fd3-cd7460b0faa7/image.png)

**사용할 패키지 import 받기**

![](https://velog.velcdn.com/images/lurelight/post/f5d0f194-6f30-4977-9773-7d6e754e041e/image.png)

![](https://velog.velcdn.com/images/lurelight/post/6bd445e8-d99a-456c-a0aa-387cec95a0b4/image.png)

**csv 경로를 지정하고 불러올 파일 선택**

![](https://velog.velcdn.com/images/lurelight/post/086e12d6-f7ed-42d5-b9f0-3622ef82c4e5/image.png)

원하는 열만 지정하고 싶을 땐, usecols를 사용해서 원하는 범위 지정


df 를 쓰면 원하는 Dataframe 을 출력할 수 있다.

![](https://velog.velcdn.com/images/lurelight/post/c485b7fb-41ca-4949-84b9-24b21c26da9b/image.png)

**처음 df의 타입 정보를 확인했을 땐, Date의 정보가 object인 것을 확인할 수 있다!**

![](https://velog.velcdn.com/images/lurelight/post/d648e416-f1b3-4e13-a729-f95146bf14f1/image.png)

**pd.to_datetime(df['Date']) 를 통해 Date의 속성을 변경해주면 Date의 속성이 datetime64[ns] 로 변한 것을 확인할 수 있다.**

![](https://velog.velcdn.com/images/lurelight/post/dfe226d2-a944-43be-acb9-120248f3fe94/image.png)

**데이터 필터링을 할 범위를 지정해서 df를 출력한다. 이때 파일이 서로 헷갈리는 걸 방지하기 위해 df_after_2021로 변경해준다.**

![](https://velog.velcdn.com/images/lurelight/post/0eae2d1a-0871-4faa-8c2c-4aa6d3ed6bb1/image.png)

![](https://velog.velcdn.com/images/lurelight/post/1b06c030-ced3-4bd2-9fc6-8930735d2b40/image.png)

![](https://velog.velcdn.com/images/lurelight/post/4bf65f17-9246-4880-b82b-580ca9ce3cbf/image.png)

![](https://velog.velcdn.com/images/lurelight/post/6ced1bca-f95c-4907-99aa-9b99d5845e6c/image.png)

![](https://velog.velcdn.com/images/lurelight/post/fa1f9a46-eda1-412d-93d8-602535361da1/image.png)

df_after_2021_max = df_after_2021.Close.max()

df_after_2021_min = df_after_2021.Close.min()

을 사용해서 최고 종가, 최소종가를 구한다!

![](https://velog.velcdn.com/images/lurelight/post/3e02771f-1280-4034-82e6-528a94722dad/image.png)

여전히 데이터 타입은 유지되어야 한다!

![](https://velog.velcdn.com/images/lurelight/post/203013f9-0cc8-4df9-b5b0-a5511bb3a6f3/image.png)

![](https://velog.velcdn.com/images/lurelight/post/fd58414e-9a56-4595-915c-a7434211bb3a/image.png)

**월별 그룹화를 위해 strftime()함수를 사용해서 년도와 월로만 나타내야 한다. 그리고 이렇게 변경한 요소를 'Date_month'라는 열로 추가한다.**

![](https://velog.velcdn.com/images/lurelight/post/d5870f1b-91d6-4c66-b173-7b27573a0bb1/image.png)

'Date_month'로 그룹화 한 데이터를 더한 값을 정리한 데이터 이다!

![](https://velog.velcdn.com/images/lurelight/post/34a642eb-7801-41bb-b8f9-673409fab0c7/image.png)

![](https://velog.velcdn.com/images/lurelight/post/9bf131b9-9695-4ea2-b94f-feba138e6e53/image.png)

월별 그룹화 한 그래프로 나타내면 위와 같다

아래 내용은 정확한 정답이 나오진 않았지만, 그래도 그래프가 나름 그려졌다!

![](https://velog.velcdn.com/images/lurelight/post/a1a7a314-b178-478e-85ea-cd5cfeacd017/image.png)

![](https://velog.velcdn.com/images/lurelight/post/4a646d2c-93b5-408f-ad2a-d55a2837fc6c/image.png)

![](https://velog.velcdn.com/images/lurelight/post/22e058c1-09eb-412d-938d-983823d795a3/image.png)

![](https://velog.velcdn.com/images/lurelight/post/b13d4240-2bae-4b6b-b07d-772fe20d1ac2/image.png)

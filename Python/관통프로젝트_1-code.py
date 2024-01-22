# 변수 사용법

# 파이썬

# 서버로부터 데이터를 가져와보세요

# https://fakestoreapi.com/carts

# 서버로부터 데이터 요청을 보내야 함
# 실제로 정상적인지 판단
# --> 보안에 위험
# 출력
# 실제로 정상적인지 판단

# 라이브러리 : 남들이 만들어놓은 코드를 가져다가 쓰자!

# 데이터를 가져오는 python 라이브러리 : requests

# 패키지를 다운로드 받기

# 파이썬 패키지 관리 : pip
# pip 를 이용해서 requests 를 설치
    # 설치 : pip install <패키지 이름>
    # 목록 확인 : pip list

# 내 코드에 다른 패키지를 추가

import requests
import pprint

api_key = '87246d75e1ce26e1392a087b3d1d88c5'
'3b8d04c57c537104d4d8cc8dcc92ff1f'


# 서울의 위도

lat = 37.56

# 서울의 경도

lon = 126.97

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'

data = requests.get(url).json() # json은 파일을 변환한 것

pprint.pprint(data['name'])

pprint.pprint(data['weather'])

pprint.pprint(data['weather'][0]['description'])
# 내 파일 검색 or 내장 모듈 모아둔 곳 검색
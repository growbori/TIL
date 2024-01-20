import pprint
import requests

# 전체 정기예금의 응답을 json 형태로 변환하여 key 값만 출력하시오.
# 공식문서의 요청변수와 예제 요청결과(JSON) 부분을 참고합니다.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터에 모든 정보가 담겨 있습니다.
# 3. key 값이 "result" 인 데이터의 key 값만 출력합니다.

def get_deposit_products():
  # 본인의 API KEY 로 수정합니다.
    api_key = "0df7858bc42fc0d4283dd9d03006a81e"

  # 요구사항에 맞도록 이곳의 코드를 수정합니다.

    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
 
    result = requests.get(url).json()

    result = result['result']['optionList'] # 'result 아래의 값들 중 'optionlist'에 해당하는 값들만 불러오기

    result_len = len(result) # for 문을 돌리기 위해서 전체 result의 길이 구하기

    new_dict = [] # result 에서 원하는 값들만 골라내서 list 형태로 정리하기 위해 빈 리스트 생성

    for i in range(result_len):
        
        new_dict.append({'금융상품코드' : result[i]['fin_co_no'], '저축 금리' : result[i]['intr_rate'], '저축 기간' : result[i]['intr_rate2'], '저축금리유형' : result[i]['intr_rate_type'], '저축금리유형명' : result[i]['intr_rate_type_nm'], '최대 우대금리' : result[i]['save_trm']})

    return new_dict  # 구하고자 하는 값들을 new_dict에 append함 (list 에 요소들을 추가하기 위해선 append를 사용해야 함)

pprint.pprint(get_deposit_products()) # get_deposit_products 함수에서 new_dict 값들을 리턴 받았으니, 그 값들을 pprint 함수를 사용해서 예쁘게 정리!
    

# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)
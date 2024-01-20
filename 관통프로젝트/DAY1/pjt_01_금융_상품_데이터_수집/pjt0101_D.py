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

    result_len = len(result['result']['baseList']) # 'result 아래의 값들 중 'baselist'에 해당하는 값들만 불러오기

    result_opt = result['result']['optionList'][0]['fin_co_no'] # 'result 아래 'optionlist' 에서 금융 상품 코드가 같으면 출력한다는 조건을 구하기 위해 optionlist 하위의 금융 상품 코드인 'fin_co_no'를 정리한다.

    result_main = result['result']['baseList'][0]['fin_co_no'] # 'result 아래 'baselist' 에서 금융 상품 코드가 같으면 출력한다는 조건을 구하기 위해 baselist 하위의 금융 상품 코드인 'fin_co_no'를 정리한다.


    value = [] # 리스트 안에 있는 딕셔너리에 또 리스트 값을 나타내기 위해 빈 리스트를 생성한다.

    for i in range(result_len):
        if result_opt == result_main: # 금융 상품코드가 같으면 출력한다는 조건문을 작성한다.
        
            value.append({'저축 금리' : result['result']['optionList'][i]['intr_rate'], '저축 기간' : result['result']['optionList'][i]['intr_rate2'], '저축금리유형' : result['result']['optionList'][i]['intr_rate_type'], '저축금리유형명' : result['result']['optionList'][i]['intr_rate_type_nm'], '최대 우대금리' : result['result']['optionList'][i]['save_trm']})

    info = [] # 바깥에 있는 리스트에 한번 더 정리하기 위해 빈 리스트를 생성한다.

    for i in range(len(value)): # 아까 정리한 value의 길이(크기) 만큼만 for 문을 돌리면 되므로 해당 범위로 설정한다.
    
        info.append({'금리정보' : value, '금융상품명' : result['result']['baseList'][i]['fin_prdt_nm'], '금융회사명' : result['result']['baseList'][i]['kor_co_nm']})

    pprint.pprint(info) # 최종! 구하고자 하는 데이터를 구한다!

    

# pprint.pprint(get_deposit_products())
    
# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    # pprint.pprint(result)

# new_dict_main['금융회사명'] = result_main[i]['kor_co_nm']
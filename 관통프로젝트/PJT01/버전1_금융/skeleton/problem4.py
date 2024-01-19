import pprint
import requests

def get_deposit_products():
  # 본인의 API KEY 로 수정합니다.
    api_key = "0df7858bc42fc0d4283dd9d03006a81e"

  # 요구사항에 맞도록 이곳의 코드를 수정합니다.

    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
 
    result = requests.get(url).json()

    result_main = result['result']['baseList']

    result_option = result['result']['optionList']

    result_len_opt = len(result_option)

    result_len_main = len(result_main)

    new_dict_opt = {}

    new_dict_main = {}

    for i in range(result_len_opt):
        new_dict_opt['금융상품코드'] = result_option[i]['fin_co_no']
        new_dict_opt['저축 금리'] = result_option[i]['intr_rate']
        new_dict_opt['저축 기간'] = result_option[i]['intr_rate2']
        new_dict_opt['저축금리유형'] = result_option[i]['intr_rate_type']
        new_dict_opt['저축금리유형명'] = result_option[i]['intr_rate_type_nm']
        new_dict_opt['최대 우대금리'] = result_option[i]['save_trm'] 

        # print(new_dict_opt)
    won = []

      for i in range(result_len_main):
        new_dict_main['금융회사명'] = result_main[i]['kor_co_nm']
        new_dict_main['금융상품명'] = result_main[i]['fin_prdt_nm']
        new_dict_main['금리정보'] = result_main[i]['mtrt_int']

        won.append({'금융회사명' : result_main[i]['kor_co_nm'], '금융상품명' : result_main[i]['fin_prdt_nm'], '금리정보' : result_main[i]['mtrt_int']})
        
        print(won)
        
        pprint.pprint(get_deposit_products())  
        
        # print(new_dict_main)
        won = []
        # if new_dict_main['fin_co_no'] == new_dict_opt['fin_co_no']:
        #     won.append({'금융회사명' : result[i]['fin_co_no'],)
            
        
    
# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)

    # 금융회사명 = 'kor_co_nm'
    # 금융상품명 = 'fin_prdt_nm'
    # 금리정보 = 'mtrt_int'
    # 'fin_co_no'이게 같아야 함
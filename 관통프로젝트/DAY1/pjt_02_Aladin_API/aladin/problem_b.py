import json
from pprint import pprint



def book_info(book, categories):

    cata_Name = []
    for i in range (len(categories)):
        for j in range(len(book['categoryId'])):

            if book['categoryId'][j] == categories[i]['id']:

                cata_Name.append(categories[i]['name']) # 문학, 영미소설 둘다 들어오게 하는 방법 고민해보기!
                
                book_data = {'author' : book['author'], 'categoryName' : cata_Name, 'cover' : book['cover'], 'description' : book['description'], 'id' : book['id'], 'priceSales' : book['priceSales'], 'title' : book['title']}

    return book_data
 




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))

import json
from pprint import pprint


def books_info(books, categories):
    cata_Name = []
    books_data = []
    for i in range (0, len(categories)):
        for j in range(len(books[0]['categoryId'])):

            if books[0]['categoryId'][j] == categories[i]['id']:
                cata_Name.append(categories[i]['name']) # 문학, 영미소설 둘다 들어오게 하는 방법 고민해보기!
                
                for k in range(len(books[0])):
                    books_data.append({'author' : books[k]['author'], 'categoryName' : cata_Name, 'cover' : books[k]['cover'], 'description' : books[k]['description'], 'id' : books[k]['id'], 'priceSales' : books[k]['priceSales'], 'title' : books[k]['title']})

    return books_data


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(books_info(books, categories_list))

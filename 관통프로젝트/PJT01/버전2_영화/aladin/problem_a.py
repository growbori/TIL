import json
from pprint import pprint


def book_info(book):

    book_data = {'author' : book['author'], 'categoryId' : book['categoryId'], 'cover' : book['cover'], 'description' : book['description'], 'id' : book['id'], 'priceSales' : book['priceSales'], 'title' : ['title']}

    return book_data



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    pprint(book_info(book))

import requests
from bs4 import BeautifulSoup
# from fake_useragent import UserAgent
# from pprint import pprint
import json

url = 'https://books.toscrape.com'

# ua = UserAgent()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

page = 1

session = requests.session()

all_books = []

while True:
    response = session.get(url + '/catalogue/page-'  + str(page) + '.html', headers=headers)
    soup = BeautifulSoup(response.text, features='html.parser')
    books_links = soup.find_all('article', {'class': 'product_pod'})

    for books_link in books_links:
        books = {}
        book_href = books_link.find('a')
        link_book = url + '/catalogue/' + book_href.get('href')

        response = session.get(link_book, headers=headers)
        soup_book = BeautifulSoup(response.text, features='html.parser')

        books_info = soup_book.find('div', {'class': 'product_main'})
        books['title'] = books_info.findChildren('h1')[0].getText()
        books['price'] = books_info.findChildren('p')[0].getText()[1:]
        books['in stock'] = int(books_info.findChildren('p')[1].getText().split()[2][1:])

        books_description = soup_book.find('article', {'class' : 'product_page'})
        books['description'] = books_description.findChildren('p')[3].getText()
        all_books.append(books)

        print(f'Отработал книгу: {books['title']}')

    print(f'Отработал страницу: {page} страницу')

    if len(soup.find_all('li', {'class': 'next'})) == 0:

        break

    page += 1

# pprint(all_books, sort_dicts=False)

with open('result.json', 'w', encoding='utf-8') as file:
    json.dump(all_books, file)
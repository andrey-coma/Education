from pprint import pprint
import requests
from lxml import html
import csv

url = 'https://news.mail.ru'

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36'
}

session = requests.session()

response = session.get(url, headers=headers)
dom = html.fromstring(response.text)

# собираем ссылки топовых новостей (8 новостей)
links = dom.xpath("//div[@class='e1c482c4c8']//a/@href")

news_top = []

# проходим по ссылкам и собираем название новости, ссылку, анонс и источник новости
for link in links:
    news = {}

    response = session.get(link, headers=headers)
    dom = html.fromstring(response.text)

    news['title'] = dom.xpath("//header//h1/text()")[0]
    news['news_link'] = link
    news['anons'] = str(dom.xpath("//header//p/text()")[0]).replace('\xa0', ' ')  # приводим к строке и удаляем неразрывный пробел (\xa0)
    news['source'] = dom.xpath("//span[@data-qa='Text']//a/text()")[0]

    news_top.append(news)

# pprint(news_top, sort_dicts=False)
# print(len(news_top))


# сохраняем полученные новости в csv файл
with open('result.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(('title','news_link','anons', 'source'))

    for new in news_top:
        writer.writerow((new['title'],new['news_link'],new['anons'], new['source']))
from pymongo import MongoClient
import json

client = MongoClient({'localhost': 27017})
db = client['books']
info = db.info

# Чтение json файла с предыдущего урока
with open('../les_2/result.json', 'r') as f:
    books = json.load(f)

# Запись в базу mongodb
for book in books:
    info.insert_one(book)


# Запросы
for book in info.find(
    # Выведем книги дороже 50 и не выводим поля (id, description)
    # {'price': {'$gt': 50}}, {'_id': 0, 'description': 0},

    # Выведем книги дороже 55 и которых на остатке < 3
    {'price': {'$gt': 55}, 'in stock': {'$lt': 3}}, {'_id': 0, 'description': 0},

    # Выведем все книги в названии которых есть слово 'Black'
    # {'title': {'$regex': 'Black'}},  {'_id': 0, 'description': 0}

):

    print(book)

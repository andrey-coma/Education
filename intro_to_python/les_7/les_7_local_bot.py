from pprint import *
from random import *
import json

commands: [dict[str]] = {
    '/exit': 'Завершение работы бота...',
    '/help': 'Просмотр доступных команд:',
    '/show': 'Просмотреть список фильмов:',
    '/add': 'Добавить новый фильм:',
    '/del': 'Удалить фильм:',
    '/rand_film': 'Показать случайный фильм:',
    '/len_films': 'Показать количество фильмов в библиотеке:',
    '/save': 'Сохраняем список фильмов...',
    '/load': 'Загружаем фильмы...'
}

data_films :list[str] = []

def save_films():
    with open('save_user_film.json', 'w', encoding='utf-8') as fl:
        fl.write(json.dumps(data_films, ensure_ascii=False))
    print('Данные успешно сохранены в файле "save_user_film.json"')

def load_films():
    global data_films
    with open('save_user_film.json', 'r', encoding='utf-8') as fl:
        data_films = json.load(fl)
    print('Данные успешно загружены')

try:
    load_films()

except FileNotFoundError:
    print('Ошибка чтения файла "save_user_film.json" или файла не существует')
    print('Данные загружены по умолчанию')
    data_films: [list[str]] = ['В поле зрения (1 сезон)', 'В поле зрения (2 сезон)', 'В поле зрения (3 сезон)',
                               'В поле зрения (4 сезон)', 'В поле зрения (5 сезон)']

print('Вас приветствуют "бот-фильмOFF"!!!')
while True:
    command: [str] = input(f'Ожидаю команду: ')
    if command == '/exit':
        save_films()
        print(commands[command])
        break

    elif command == '/show':
        print(commands[command])
        pprint(f'{data_films}')

    elif command == '/help':
        print(commands[command])
        pprint(commands)

    elif command == '/add':
        print(commands[command])
        add_film: [str] = input(f'Введите новый фильм: ')
        if add_film not in data_films:
            data_films.append(add_film)
            print(f'Фильм "{add_film}" - успешно добавлен')
        else:
            print(f'Фильм "{add_film}" - уже есть')

    elif command == '/del':
        print(commands[command])
        del_film: [str] = input(f'Введите фильм для удаления: ')
        if del_film in data_films:
            data_films.remove(del_film)
            print(f'Фильм "{del_film}" - успешно удален')
        else:
            print(f'Фильма "{del_film}" - не существует')

    elif command == '/rand_film':
        pprint(commands[command])
        print(choice(data_films))

    elif command == '/len_films':
        print(commands[command])
        print(len(data_films))

    elif command == '/save':
        print(commands[command])
        save_films()

    elif command == '/load':
        print(commands[command])
        load_films()

    else:
        print(f'{command} - недопустимая команда')
        print('Для просмотра доступных команд введите - "/help"')
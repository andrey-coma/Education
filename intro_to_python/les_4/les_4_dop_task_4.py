"""
ДОП задание Поход желанию

Три друга взяли вещи в поход.
Имеется словарь, где ключ - имя друга, а значение - кортеж вещей.
Ответьте на вопросы:

какие вещи взяли все три друга - "спички"

какие вещи уникальны, есть только у одного друга - Лиза взяла косметичку, Вася взял топор, Ваня взял еду

какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует - у Лизы нет спальника,

Код должен расширяться на любое большее количество друзей.
"""

import pprint

menu = {
    1: 'какие вещи взяли все друзья?',
    2: 'какие вещи уникальны, есть только у одного друга?',
    3: 'какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует?',
    4: 'выбирите - 4, чтобы добавить нового друга',
    5: 'для просмотра друзей (вещей)'
    }

hike = {
    'Вася': ("спички", "спальник", "дрова", "топор"),
    'Ваня': ("спальник", "спички", "вода", "еда"),
    'Лиза': ("вода", "спички", "косметичка"),
    }

result_things = []  # список всех вещей + дубли
template = {'Имя нового друга': ('новые передметы', )}  # шаблон для нового друга
new_friend = {}  # словарь для нового друга


# Функция обновления списка вещей
def update_things():
    result_things.clear()
    for data_things in hike.values():
        for i in data_things:
            result_things.append(i)

    return result_things


res = set()


# Функция ноплнения множества вещей в зависимости от вопроса question
def all_things(num_question):
    res.clear()
    for thing in update_things():
        if result_things.count(thing) == num_question:
            res.update({thing})

    return res


pprint.pprint(menu)
print()

while True:
    print('для вызова вопросов выбрать - 6')
    question = input('Выбирите номер вопроса или 0 для выхода: ')
    print()

    if question == '0':  # завершения работы программы
        break

    if question == '5':  # печать списка друзей
        pprint.pprint(hike)
        print()

    if question == '6':  # печать списка вопросов
        pprint.pprint(menu)
        print()

    if question == '1':  # какие вещи взяли все друзья?
        question = len(hike)
        if len(all_things(question)) != 0:
            print(f'{all_things(question)} - есть у всех')
        else:
            print('Таких нет')
        print()

    if question == '2':  # какие вещи уникальны, есть только у одного друга?
        question = 1
        if len(all_things(question)) != 0:
            print(f'{all_things(question)} - уникальные вещи')
        else:
            print('Таких нет')
        print()

    if question == '3':  # какие вещи есть у всех друзей кроме одного
        question = len(hike) - 1
        if len(all_things(question)) == 0:
            print('Таких нет')

        for item in res:
            for name, things in hike.items():
                if item not in things:
                    print(f'{name}, нет {item}')  # и имя того, у кого данная вещь отсутствует
        print()

    if question == '4':  # добавить нового друга'
        new_friend.clear()
        for key, value in template.items():
            while True:
                name = input(f'{key}: ').capitalize()
                if name.isalpha():
                    friend_thing = input(f'Введите {value[0]} (через пробел): ').lower().split()
                    new_friend[name] = tuple(friend_thing)
                    hike.update(new_friend)
                    break

                else:
                    print('Имя не может содержать цифры!')
                    continue

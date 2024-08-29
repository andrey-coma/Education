"""
Палиндром
Пользователь вводит строку. Необходимо написать программу, которая
определяет, существует ли у этой строки перестановка, при которой она станет палиндромом.
Затем она должна выводить соответствующее сообщение.

Пример 1
Введите строку: aab
Можно сделать палиндромом

Пример 2
Введите строку: aabc
Нельзя сделать палиндромом
"""

from collections import Counter
import random
import pprint

# Для проверки, можно ли получить палиндром, функция can_be_poly вычисляет количество символов с
# нечетной частотой и проверяет, что их количество меньше 2. Это условие указывает на то, что строка может быть
# переставлена в палиндром.
def can_be_poly(message: str) -> bool:
    result = list(filter(lambda x: x % 2, Counter(message).values()))
    if len(result) < 2:
        return True
    else:
        return False

mes = 'abbbc'

count = 1000 # кол-во подборов
options = [] # Возможные варианты палиндромов

if mes.count(' '):
    print('В вашей строке есть пробелы')

if can_be_poly(mes):
    # подбор полиндрома
    for _ in range(count):
        res = ''
        lets = [i for i in mes] # перезаполняем список значениями при каждой итерации в цикле while
        for _ in range(len(lets)):
            rand_let = random.choice(lets) # случайно определяем букву из списка lets
            res += lets.pop(lets.index(rand_let)) # сохр. получ. букву и удал-м ее из lets, для исключения повтора

        if res == res[::-1]:
            options.append(res)  # сохраняем подходящие варианты
else:
    print(f"Нельзя сделать палиндромом - {mes}")


print(f'Возможные варианты палиндромов - {len(set(options))}:')
pprint.pprint(f'{set(options)}')
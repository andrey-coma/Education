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

import random
import pprint

a = 'bababab'

count = 10000 # кол-во подборов
attempt = 0 # попытка
uns_options = [] # Неподходящие варианты
if a.count(' '):
    print('В вашей строке есть пробелы')

else:
    while True:
        if count == 0:
            print(f"Нельзя сделать палиндромом - {a}")
            break

        res = ''
        lets = [i for i in a] # перезаполняем список значениями при каждой итерации в цикле while
        for _ in range(len(lets)):
            rand_let = random.choice(lets) # случайно определяем и выбираем букву из списка lets
            res += lets.pop(lets.index(rand_let)) # сохр-ем получ. бук. и удал-м ее из lets, чтобы она снова нам не попалась

        if res == res[::-1]:
            print(f"Можно сделать палиндромом {a} - {res}")
            break

        else:
            uns_options.append(res)  # сохраняем неподходящие варианты

        count -= 1
        attempt += 1

print(f'попытка - {attempt + 1}')
print(f'Неподходящие варианты - {len(set(uns_options))}:')
pprint.pprint(f'{set(uns_options)}')
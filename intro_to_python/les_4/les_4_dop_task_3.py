'''
Задача Де моргана необязательная

Тут вам пригодятся библиотеки random и time

Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

теперь надо проверить ее практически
в цикле 100 раз прогоняем
каждый раз генерируем случайное количество предикат от 3 до 15
и конечно со случайным булевым значением
и засекаем общее время выполнения программы
юзаем библиотеки random и time
предикаты НЕ ЗАДАЕМ как целое число!

например, при первом эксперименте количество предикат сгенерировалось равным 4
тогда получили 4 предикаты со случайным значением и например это [True, False, False, True]
проверили равенство левой части и правой части теоремы де Моргана применительно к этим предикатам,
если все ок, то переходим к другому эксперименту, если теорема нарушается, то вывести всю информацию об этом

в конце написать сколько времени отработал ваш код.
'''

import time
import random

# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# not(X and Y and Z) == (not X) or (not Y) or (not Z)
# path_left, path_right = not(X and Y and Y), (not X) or (not Y) or (not Z)
start_time = time.time()

count = 1000  # счетчик итераций
equality_true = 0  # счетчик выполнения теоремы
exp = 0  # счетчик экспериментов
n = 100  # количество генераций
rand_predicate = []  # список случайных предикатов

while count:
    for _ in range(n + 1):
        rand_predicate = [random.choice([True, False]) \
                     for _ in range(random.randint(3, 15))]

    left = []
    right = []
    for _ in range(3):
        left.append(random.choice(rand_predicate))
        right.append(random.choice(rand_predicate))

    # print(left, right)

    equality = not(left[0] and left[1] and left[2]) \
                 is (not right[0]) or (not right[1]) or (not right[2])

    if equality:
        equality_true += 1

    count -= 1
    exp += 1

total_time = time.time() - start_time

print(f'экспериментов - {exp}')
print(f'теорема де Моргана выполняется - {equality_true}')
print(f'теорема де Моргана нарушается - {exp - equality_true}')

print(f'{round(total_time, 5)} - сек.')

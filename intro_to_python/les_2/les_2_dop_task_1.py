"""
Допзадание 1 - Пользователь вводит любое число (дробное или целое),
надо посчитать количество цифр в числе.
Решаем строго математически, обращаться к числу как к строке нельзя.

0 -> 1
9 -> 1
56.77 -> 4
-0.0001 - > 5
100.18006 ->8
"""

from decimal import *

while True:
    try:
        num = Decimal(input('Введите любое число: '))

        if isinstance(num, Decimal):
            num = abs(num)
            tmp = num
            break

    except ValueError:
        print(f'это не число!')

if num < 1:  # если дробь меньше 1 или 0, тогда + 1
    num += 1

if isinstance(num, Decimal):  # Преобразуем дробную часть в целую
    while True:
        if num % 1 == 0:
            num = int(num)  # Преобразуем дробь без хвоста в int
            break
        num *= 10
        num = num.quantize(Decimal(tmp))

# Считаем цифры

print(num)

total = 0

while num:
    total += 1
    num //= 10

print(total)
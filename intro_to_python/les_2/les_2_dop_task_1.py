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

while True:
    try:
        num = float(input('Введите любое число: '))

        if isinstance(num, float):
            num = abs(num)
            break

    except ValueError:
        print(f'это не число!')

if num < 1:  # если дробь меньше 1 или 0, тогда + 1
    num += 1

if isinstance(num, float):  # Преобразуем дробную часть в целую
    while True:
        if num % 1 == 0:
            num = int(num)  # Преобразуем дробь без хвоста в int
            break
        num *= 10
        num = round(num, 5)

# Считаем цыфры

print(num)

total = 0

while num:
    total += 1
    num //= 10

print(total)

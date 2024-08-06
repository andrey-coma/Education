"""
Задача 1 НЕГАФИБОНАЧЧИ по желанию

Задайте число.

Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

для k = 9
список будет выглядеть так:


[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]"""


num = 9

# способ 1

result = [1, 0, 1]

for i in range(num - 2):
    result.append(result[-1] + result[-2])
    result.insert(0, result[-1] * ((-1) ** (i + 1)))

print(result)


# способ 2 (с чистым исходным списком)

num_1 = 1
num_2 = 0
res = []

for _ in range(1, (num * 2)):
    if _ < num:
        num_1 -= num_2
        res.insert(0, num_1)
    else:
        num_1 += num_2
        res.append(num_1)

    num_1, num_2 = num_2, num_1

    if _ == num - 1:
        num_1 = -1
        num_2 = 1

print(res)

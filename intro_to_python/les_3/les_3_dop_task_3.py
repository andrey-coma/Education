"""
Задача 3 Спираль необязательная

Выведите таблицу размером n×n, заполненную числами от 1 до n**2 по спирали,
выходящей из левого верхнего угла и закрученной по часовой стрелке,
как показано в примере (здесь n=5):

1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
"""


num = 3

matrix = [num * [0] for i in range(num)]  # заполняем матрицу num * num нулями - '0'

# for i in matrix:
#     print(*i)

start = 0
count = 1

while start < num // 2:
    n = num - start * 2 - 1  # смещение на -1 для range при полном цикле

    # заполняем по оси x
    for x in range(n):
        matrix[start][x + start] = count
        count += 1

    # заполняем по оси y
    for y in range(n):
        matrix[start + y][num - start - 1] = count
        count += 1

    # заполняем по оси x
    for x in range(n):
        matrix[num - start - 1][num - start - x - 1] = count
        count += 1

    # заполняем по оси y
    for y in range(n):
        matrix[num - start - y - 1][start] = count
        count += 1

    start += 1  # смещение по индексам
    # num //= 2

if num % 2 == 1:  # выравнивание для нечетых матриц
    matrix[start][start] = count


for i in matrix:
    print(*i)

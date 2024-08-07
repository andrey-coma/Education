"""
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
На вход подается 2 числа через пробел: n m
n - кол-во элементов первого множества.
m - кол-во элементов второго множества.
Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо

Пример

На входе:

var1 = '5 4' # количество элементов первого и второго множества
var2 = '1 3 5 7 9' # элементы первого множества через пробел
var3 = '2 3 4 5' # элементы второго множества через пробел

На выходе:

3 5

"""

var1 = '5 4'  # количество элементов первого и второго множества
var2 = '1 2 3'  # элементы первого множества через пробел
var3 = '1 2 3 4'  # элементы второго множества через пробел

# n, m = var1.split(' ')
# print(n, m)

# 1 способ

res = set(var2.split(' ')) & (set(var3.split(' ')))

print(*sorted(res))


# более оптимальынй способ
# метод sort() немного быстрее и потребляет на 24% меньше памяти
# https://python-scripts.com/sort-list

res = list(set(var2.split(' ')) & (set(var3.split(' '))))

res.sort()
print(*res)

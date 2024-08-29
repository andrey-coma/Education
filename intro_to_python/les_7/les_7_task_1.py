# Задание 1. Новые списки
# Даны три списка:
# 1. floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
# 2. names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
# 3. numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]
# Напишите код, который создаёт три новых списка. Вот их содержимое:
# 1. Каждое число из списка floats возводится в третью степень и округляется
# до трёх знаков после запятой.
# 2. Из списка names берутся только имена минимум из пяти букв.
# 3. Из списка numbers берётся произведение всех чисел.

from functools import reduce

floats: list[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: list[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: list[int] = [22, 33, 10, 6894, 11, 2, 1]

# 1 map
print(list(map(lambda x: round(x ** 3, 3), floats)))

# 2 filter
print(list(filter(lambda x: len(x) >= 5, names)))

# 3 reduce
print(reduce(lambda x, y: x * y , numbers))

# 4 zip
print(*list(zip(names, floats, numbers)))
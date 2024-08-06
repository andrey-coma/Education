"""
Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.

Пример:

list_1 = [1, 2, 3, 4, 5]
k = 6
# 5

"""

list_1 = [1, 2, 3, 4, 5]
k = 6



# 2 способ

result = 0

for i in list_1:
    if i == k:
        result = i
        break
    elif abs(i - k) == 1:
        result = i
    elif i - 1 == k:
        result = i

print(result)


# способ GB

# m = abs(k - list_1[0])
#
# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)

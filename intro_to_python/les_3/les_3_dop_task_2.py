"""
Задача 2 Последовательность необязательная

Имеется список случайных целых чисел. Создайте список,
в который попадают числа, описывающие максимальную сплошную возрастающую последовательность.

Порядок элементов менять нельзя.

Одно число - это не последовательность.

Пример:

[1, 5, 2, 3, 4, 6, 1, 7] => [1, 7] /

                    так как здесь вразброс присутствуют все числа от 1 до 7

[1, 5, 2, 3, 4, 1, 7, 8, 15, 1] => [1, 5] /

                    так как здесь есть числа от 1 до 5 и эта последовательность длиннее чем от 7 до 8


[1, 5, 3, 4, 1, 7, 8, 15, 1] => [3, 5] /
                    так как здесь есть числа от 3 до 5 и эта последовательность длиннее чем от 7 до 8

"""

nums = [1, 107, 5, 17, 3, 4, 4, 106, 1, 7, 8, 15, 1, 16, 100, 5, 101, 102, 18, 105, 103, 104, 108]

# 1 способ (не сомое лучшее решение)

# найдем мин. и макс. число последовательности

num_min = max(nums)
num_max = 0

for i in nums:
    if i + 1 in nums:
        if num_max < i + 1:
            num_max = i + 1
        if num_min > i + 1:
            num_min = i

print(f'Встречаются послед-ти: от {num_min} до {num_max}')

# найдем все возможные последовательности

count = 0
index = 0
res = [[]]

for item in range(num_min, num_max + 1):
    if item in nums:
        res[index].append(item)
        count += 1

    if (item not in nums) and (count != 0):
        count = 0
        index += 1
        res.append([])

print(*res)

# найдем максимальную последовательность

total = []
max_len = 0

for i in res:
    if max_len < len(i):
        max_len = len(i)
        total = i

print([total[0], total[-1]])


"""
# способ 2 (очень замороченный вариант с использованием set)

nums = [1, 5, 3, 4, 1, 7, 8, 15, 1]

tmp = list(set(nums))
print(tmp)

count = 0
index = 0
res = [[]]

for idx, item in enumerate(tmp, 1):
    if item == tmp[-1]:
        if count != 0:
            res[index].append(item)
        if [] in res:
            res.remove([])
        break

    if tmp[idx] - item == 1:
        res[index].append(item)
        count += 1

    if tmp[idx] - item > 1 and count != 0:
        res[index].append(item)
        count = 0
        index += 1
        res.append([])

print(*res)

total = []
max_len = 0

for i in res:
    if max_len < len(i):
        max_len = len(i)
        total = i

    total = [min(total), max(total)]

print(total)
"""
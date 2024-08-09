"""
Задача Сортировка необязательная

Задайте двумерный прямоугольный список из целых чисел.
Количество строк и столбцов задается с клавиатуры.
Отсортировать элементы по возрастанию слева направо и сверху вниз.

Например, задан cписок:
[[1 4 7 2],
[5 9 10 3]]

После сортировки
[[1 2 3 4],
[5 7 9 10]]
"""


# Ввод строк и столбцов массива
while True:
    lines = input(f'Введите кол-во строк массива: ')
    if lines.isdigit():
        lines = int(lines)
        row = input(f'Введите кол-во столбцов массива: ')
        if row.isdigit():
            row = int(row)
            break

        else:
            print(f'из целых чисел!')

arr = []  # массив
# Ввод елементов массива
for index in range(lines):
    arr.append([])
    for num_arr in range(row):
        while True:
            tmp = input(f'{num_arr + 1} из {row} элементов массива {index + 1}: ')
            if tmp.isdigit():
                arr[index].append(int(tmp))
                break

            else:
                print(f'из целых чисел!')

print('*' * 25)
print('Массив до сортировки')
for i in arr:
    print([i])
print('*' * 25)

# arr = [[1, 9, 6], [3, 2, 0], [7, 15, 4]]
# arr = [[7, 5, 1]]

count = 0  # счетчик проходов

while count < len(arr[0]) * len(arr):  # максимальное кол-во проходов требуемое для окончательной сортировки массива:
    if len(arr) == 1:  # если в массиве 1 элемент, сортируем на месте и выходим из цикла
        arr[0].sort()
        break

    for idy, item in enumerate(arr):  # итерируемся по спискам
        if idy == len(arr) - 1:  # при достижении перд.последнего индекса спискОВ обнуляем индекс
            idy = 0

        for idx, _ in enumerate(item):  # итерируемся по элементам списков
            if idx == len(item) - 1:  # при достижении пред.последнего индекса спискА обнуляем индекс
                idx = 0

            if item[idx] > item[idx + 1]:  # сортировка внутри списка
                item[idx], item[idx + 1] = \
                    item[idx + 1], item[idx]

            elif arr[idy][-1] > arr[idy + 1][0]:  # сортировка м/д списками (м/д послед. и 1 элементом след. списка)
                arr[idy][-1], arr[idy + 1][0] = \
                    arr[idy + 1][0], arr[idy][-1]

    count += 1

print(f'Выполнено за {count} проходов')

print()
for i in arr:
    print([i])

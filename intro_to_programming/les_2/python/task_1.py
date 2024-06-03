'Нахождение индексов максимального и минимального элемента массива'

data_nums = [-1, 482, -5, 6, 46, 690, -405621, 45, 23, 45666660]
max_index, min_index = 0, 0

for i in data_nums:
    if data_nums[max_index] < i:
        max_index = data_nums.index(i)
    elif data_nums[min_index] > i:
        min_index = data_nums.index(i)

# print(max_index, min_index)

print(f'Максимальный индекс: {max_index}')
print(f'Минимальный индекс: {min_index}')

'Найти среднее арифметическое среди всех элементов массива.'

from statistics import mean

data_nums = [12, 4, 482, 5, 6, 46, 690, 4056, 45, 23]

# 1 способ

data_len = len(data_nums)
data_sum = sum(data_nums)

print(data_sum/data_len)

# 2 способ

print(mean(data_nums))

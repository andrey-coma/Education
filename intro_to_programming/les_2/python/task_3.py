'Найти сумму элементов массива, лежащих между максимальным и минимальным по значению элементами'

data_nums = [12, 4, 100, 50, 45, 145, 459]
sum_nums = 0

# получаем последовательности start, end
start = data_nums.index(max(data_nums))
end = data_nums.index(min(data_nums))
print(f'Индексы: {start, end}')

# Меняем местами индексы, если min индекс больше max
if end < start:
    end, start = start, end
    print(f'Индексы после замены: {start, end}')

for i in range(start + 1, end):
    sum_nums = sum_nums + data_nums[i]

print(sum_nums)
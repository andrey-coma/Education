'Задание на «разворот» массива. Нужно перевернуть массив и записать его в обратном порядке.'

data_nums = [-1, 482, 5, 56, 5]
print(data_nums)

# 1 способ

revers_num = []


for i in data_nums:
    revers_num.insert(0, i)

print(revers_num)

# 2 способ
print(data_nums[::-1])

# 3 способ

x = 0
y = -1
count_iter = len(data_nums)

while count_iter // 2:
    data_nums[x], data_nums[y] = data_nums[y], data_nums[x]
    x += 1
    y -= 1
    count_iter -= 2

print(data_nums)
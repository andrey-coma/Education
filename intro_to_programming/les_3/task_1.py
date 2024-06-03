numbers = [2, 5, 13, 7, 6, 4]

size = len(numbers)
sum_nums = 0
avg = 0
index = 0

while index < size:
    sum_nums += numbers[index]
    index += 1

avg = sum_nums / size

print(avg)
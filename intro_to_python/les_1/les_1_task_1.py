"""
Найдите сумму цифр трехзначного числа n.
Результат сохраните в перменную res.

n = 123 -> res = 6 (1 + 2 + 3)

n = 100 -> res = 1 (1 + 0 + 0)


"""

n = 123

# 1 способ с циклом

res = 0
for i in str(n):
    res += int(i)


print(res)

# 2 способ без цикла

tmp = str(n)
res = int(tmp[0]) + int(tmp[1]) + int(tmp[2])

print(res)
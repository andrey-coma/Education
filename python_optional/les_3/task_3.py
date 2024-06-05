lst = [1, 2, 3, 4, 5, 6, 7]
total = []

for i in lst:
    if not (i in total) and (lst.count(i) > 1):
        total.append(i)

print(total)
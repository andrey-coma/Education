"""
Задача 3. Двумерный список
Часто в программировании приходится писать код исходя из результата,
который требует заказчик. В этот раз ему нужно получить двумерный список:
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
Напишите программу, которая генерирует такой список и выводит его на экран.
Используйте только list comprehensions."""


result = [[i + j for i in (0, 4, 8)] for j in range(1, 5)]
print(result)


# способ БЕЗ list comprehensions
res = []
for j in (0, 4, 8):
    for idx, i in enumerate(range(1, 5)):
        try:
            if res[idx] in res:
                res[idx].append(i + j)

        except IndexError:
            res.append([i])

print(res)
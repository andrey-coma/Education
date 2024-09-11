"""
На складе лежат разные фрукты в разном количестве.
Нужно написать функцию total_fruits, которая на вход принимает любое количество названий фруктов и их количество, а возвращает общее количество фруктов на складе.

можно решить через **kwargs

Пример
После вашего кода будет добавлена следующая строка:
print(total_fruits(apples=10, bananas=5, oranges=8))
На выходе:
23
"""

def total_fruits(**kwargs) -> int:
    res = 0
    for value in kwargs.values():
        res += value
    return res

print(total_fruits(apples=10, bananas=5, oranges=8))
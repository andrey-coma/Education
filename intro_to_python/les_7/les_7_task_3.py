"""Задача 3. Палиндром
Используя модуль collections, реализуйте функцию can_be_poly, которая
принимает на вход строку и проверяет, можно ли получить из неё палиндром.
Пример кода:
print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))
Результат:
True
False
"""

from collections import Counter

def can_be_poly(message: str) -> bool:
    res = list(filter(lambda x: x % 2, Counter(message).values()))
    if len(res) < 2:
        return True

    return False

mes:[str] = 'аалл'
print(can_be_poly(mes))
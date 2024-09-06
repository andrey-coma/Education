"""
Задача 4. Генератор подстрок
Напишите генераторную функцию substrings(s), которая принимает строку
s и возвращает генератор всех возможных подстрок этой строки.

На вход подается строка abc
На выходе будут выведены обозначения:
a
ab
abc
b
bc
c
"""
from typing import *

def substrings(s: str) -> Iterator[str]:
    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            yield s[start:end]

print(*substrings('abc'))

# for i in substrings('abc'):
#     print(i)
"""
Задание 1. Квадраты чисел
Пользователь вводит число N. Напишите программу, которая генерирует
последовательность из квадратов чисел от 1 до N (1 ** 2, 2 ** 2, 3 ** 2 и так
далее).
Реализацию напишите двумя способами: функция-генератор и генераторное выражение.
"""
from typing import *

#  функция-генератор
def generator_function(n: int) -> Iterator[int]:
    for num in range(1, n + 1):
        yield num ** 2

def main() -> None:
    n = input('Введите число: ')
    if n.isdigit() is False:
        return None
    n = int(n)

    print('функция-генератор:')
    print(*generator_function(n), end=' ')

#  генераторное выражение
    print()
    print('генераторное выражение:')

    result = (num ** 2 for num in range(1, n + 1))
    print(*result)

main()
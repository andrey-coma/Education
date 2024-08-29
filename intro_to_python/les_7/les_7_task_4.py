"""
Задача 4. Уникальный шифр
Напишите функцию, которая принимает строку и возвращает количество
уникальных символов в строке. Используйте для выполнения задачи
lambda-функции и map и/или filter.
Сделайте так, чтобы алгоритм НЕ был регистрозависим: буквы разного
регистра должны считаться одинаковыми.

Пример:
message = "Today is a beautiful day! The sun is shining and the birds are
singing."

unique_count = count_unique_characters(message)

print("Количество уникальных символов в строке:", unique_count)
Вывод: количество уникальных символов в строке — 5."""

# c map, lambda
def lets_counter_map(mes: str) -> int:
    unique_count = list(map(lambda x: mes.lower().count(x) == 1, mes))

    return unique_count.count(True)

message = 'Today is a beautiful day! The suZzn is shining and the birds are'
print(lets_counter_map(message))


# c filter, lambda
def let_counter_filter(mes: str) -> int:
    unique_count = list(filter(lambda x: mes.lower().count(x) == 1, mes))

    return len(unique_count)

message = 'Today is a beautiful day! The suZzn is shining and the birds are'
print(let_counter_filter(message))

# без map, filter
from collections import Counter

def len_counter(mes: str) -> int:
    unique_count:[int] = 0
    res_count:[dict] = Counter(mes.lower())
    for count in res_count.values():
        if count == 1:
            unique_count += count

    return unique_count

message = 'Today is a beautiful day! The suZzn is shining and the birds are'
print(len_counter(message))
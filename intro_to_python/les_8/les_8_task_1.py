"""Задание 1. Сумма чисел
Во входном файле numbers.txt записано N целых чисел, которые могут быть
разделены пробелами и концами строк. Напишите программу, которая выводит
сумму чисел во выходной файл answer.txt.
Пример:
Содержимое файла numbers.txt
2
2
2
2
Содержимое файла answer.txt
8
"""

with open('les_8_txt/numbers.txt', 'r', encoding='utf-8') as file:
    res = 0
    for item in file:
        res += int(item)

with open('les_8_txt/answer.txt', 'w', encoding='utf-8') as file:
    print(res, file=file)
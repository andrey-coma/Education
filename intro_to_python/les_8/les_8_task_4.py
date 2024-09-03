"""
Задача 4. Частотный анализ
Есть файл text.txt, который содержит текст. Напишите программу, которая
выполняет частотный анализ, определяя долю каждой буквы английского
алфавита в общем количестве английских букв в тексте, и выводит результат в
файл analysis.txt. Символы, не являющиеся буквами английского алфавита,
учитывать не нужно.
В файл analysis.txt выводится доля каждой буквы, встречающейся в тексте, с
тремя знаками в дробной части. Буквы должны быть отсортированы по
убыванию их доли. Буквы с равной долей должны следовать в алфавитном
порядке.

Пример:
Содержимое файла text.txt:
Mama myla ramu.
Содержимое файла analysis.txt:
a 0.333
m 0.333
l 0.083
r 0.083
u 0.083
y 0.083"""

from collections import Counter
import re

with open('les_8_txt/text.txt', 'r', encoding='utf-8') as file:
    res = file.read()

clean_text = re.sub(r'\W', r'', res.lower())

result_counter = Counter(clean_text)

len_let = sum(value for value in result_counter.values())

with open('les_8_txt/analysis.txt', 'w', encoding='utf-8') as file:
    for key, value in result_counter.items():
        print(key, (round(value / len_let, 3)), file=file)

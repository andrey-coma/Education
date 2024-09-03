"""
Задача 5*. «Война и мир»
Мало кто не знает знаменитый роман Л. Н. Толстого «Война и мир». Это
довольно объёмное произведение лежит в архиве voina-i-mir.zip. Напишите
программу, которая подсчитывает статистику по буквам (не только русского
алфавита) в этом романе и выводит результат на экран (или в файл). Результат
должен быть отсортирован по частоте встречаемости букв (по возрастанию или
убыванию). Регистр символов имеет значение.
Архив можно распаковать вручную, но, если хотите, можете изучить
документацию по модулю zipfile (можно использовать и другой модуль) и
попробовать написать код, который будет распаковывать архив за вас."""

import zipfile
import re
from collections import Counter

with zipfile.ZipFile('les_8_txt/voina-i-mir.zip') as file_zip:
    file_name =  file_zip.namelist()

    with file_zip.open(file_name[0]) as file:
        res = file.read().decode('utf-8')

clean_text = re.sub(r'\W', '', res)

result = dict(sorted(Counter(clean_text).items(), key=lambda x: x[1], reverse=True))
print(result)

with open('les_8_txt/result.txt', 'w', encoding='utf-8') as file_result:
    print(result, file=file_result)
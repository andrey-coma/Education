"""В файле first_tour.txt записано число K и данные об участниках турнира по
настольной игре «Орлеан»: фамилии, имена и количество баллов, набранных в
первом туре. Во второй тур проходят участники, которые набрали более K
баллов в первом туре.

Напишите программу, которая выводит в файл second_tour.txt данные всех
участников, прошедших во второй тур, с нумерацией.

В первой строке нужно вывести в файл second_tour.txt количество участников
второго тура. Затем программа должна вывести фамилии, инициалы и
количество баллов всех участников, прошедших во второй тур, с нумерацией.
Имя нужно сократить до одной буквы.

Список должен быть отсортирован по убыванию набранных баллов.

Пример:
Содержимое файла first_tour.txt:
80
Ivanov Serg 80
Sergeev Petr 92
Petrov Vasiliy 98
Vasiliev Maxim 78

Содержимое файла second_tour.txt:
2
1) V. Petrov 98
2) P. Sergeev 92"""

import re

res = []
with open('les_8_txt/first_tour.txt', 'r', encoding='utf-8') as file:
    for i in file.readlines():
        res.append(i.replace('\n', ''))

K = int(res.pop(0))

all_students = {}
for i in res:
    all_students[i[:-3]] = int(i[-2:])

students_next = dict((key, value) for key, value in all_students.items() if value > K)
sort_students_next = dict(sorted(students_next.items(), key=lambda x: x[1], reverse=True))


with open('les_8_txt/second_tour.txt', 'w', encoding='utf-8') as file:
    print(len(sort_students_next), file=file)
    for idx, (key, value) in enumerate(sort_students_next.items(), 1):
        res = re.findall(r'\w+', key)
        print(str(idx) + ''.join(')'), res[1][0] + ''.join('.'), res[0], value, file=file)
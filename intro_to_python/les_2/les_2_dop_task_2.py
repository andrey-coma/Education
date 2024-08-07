"""
Валентина прогуляла лекцию по математике.
Преподаватель решил подшутить над нерадивой студенткой и
попросил ее на практическом занятии перечислить все положительные делители некоторых целых чисел.
Для несложных примеров студентка быстро нашла решения
(для числа 6 это: 1, 2, 3, 6; а для числа 16 это: 1, 2, 4, 8, 16), но этим все не закончилось.

На домашнее задание ей дали варианты посложнее: 23436, 190187200, 380457890232.
•
Решить такое вручную, как вы понимаете, практически нереально.
Вот Валентина и обратилась к вам за помощью.
Помогите ей.
Постарайтесь найти самое оптимальное решение.
Результат представьте в виде списка (не забудьте отсортировать по возрастанию).
"""

import time

num = 190187200
result = []

start_time = time.time()


for itm in range(1, int(num ** (1 / 2)) + 1):  # Оптимизация корень из числа num
    if num % itm == 0:
        result.append(itm)
        if not itm == num // itm:  # Оптимизация
            result.append(num // itm)

total_time = time.time() - start_time
print(round(total_time, 5))

print(sorted(result))

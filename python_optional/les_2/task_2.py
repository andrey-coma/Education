"""На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.
Для проверки своего кода используйте модуль fractions.
"""

import fractions

frac1 = '4/5'
frac2 = '5/6'

frac_num_1_str, frac_den_1_str = frac1.split('/')
frac_num_2_str, frac_den_2_str = frac2.split('/')

# Преобразование строки к целому числу
frac_num_1 = int(frac_num_1_str)
frac_den_1 = int(frac_den_1_str)
frac_num_2 = int(frac_num_2_str)
frac_den_2 = int(frac_den_2_str)

# сумма дробей
# Поиск общего знаменателя
denominator = 1
while True:
    if (denominator % frac_den_1 == 0) and (denominator % frac_den_2 == 0):
        break

    denominator += 1

sum_frac_num = ((denominator / frac_den_1) * frac_num_1) + ((denominator / frac_den_2) * frac_num_2)
print(f'Сумма дробей: {int(sum_frac_num)}/{denominator}')

# произведение дробей
multi_frac_num = frac_num_1 * frac_num_2
multi_frac_den = frac_den_1 * frac_den_2

print(f'Произведение дробей: {multi_frac_num}/{multi_frac_den}')

# Проверка
f1 = fractions.Fraction(int(frac1[0]), int(frac1[2]))
f2 = fractions.Fraction(int(frac2[0]), int(frac2[2]))

print(f'Сумма дробей: {f1 + f2}')
print(f'Произведение дробей: {f1 * f2}')
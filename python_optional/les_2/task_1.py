# Напишите программу, которая получает целое число num и возвращает
# его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

# 1 способ

num = int(input('Введите число: '))
num_ex = num
base = int(input('Введите систему счисления: '))
result_tmp = ''
result_num = ''
hex_num = {'10': 'a', '11': 'b', '12': 'c', '13': 'd', '14': 'e', '15': 'f'}

while num:
    result_tmp = str(num % base)
    if result_tmp in hex_num:
        result_num = result_tmp.replace(result_tmp, hex_num[result_tmp]) + result_num
    else:
        result_num = result_tmp + result_num
    num //= base

# print(f'Шестнадцатеричное представление числа: {result_num.upper()}')
# print(f'Проверка результата: {hex(int(num_ex))}')

print(f'Число {num_ex} в {base}-ичной системе счисления будет: {result_num}')
print(bin(num_ex) if base == 2 else hex(num_ex) if base == 16 else oct(num_ex))


# 2 способ

# HEX = 16
# hex_digits = '0123456789ABCDEF'
#
# hex_num = ''
# test_hex_num = hex(num)
#
# while num > 0:
#     remainder = num % HEX
#     hex_num = hex_digits[remainder] + hex_num
#     num //= HEX
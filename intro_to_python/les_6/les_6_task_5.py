"""
Задача 5. Шифр Цезаря
Юлий Цезарь использовал свой способ шифрования текста. Каждая буква
заменялась на следующую по алфавиту через K позиций по кругу. Если взять
русский алфавит и K, равное 3, то в слове, которое мы хотим зашифровать,
буква А станет буквой Г, Б станет Д и так далее.

Пользователь вводит сообщение и значение сдвига. Напишите программу,
которая изменит фразу при помощи шифра Цезаря.

Пример:

Введите сообщение: это питон.
Введите сдвиг: 3

Зашифрованное сообщение: ахс тлхср.
"""

alphabet_ru = sorted('йцукенгшщзхъфывапролджэячсмитьбю')
alphabet_en = [chr(i) for i in range(97, 123)]

# функция шифрование со смещением

def cripto_mes(mes: str, alph: list, shift: int) -> str:
    alph.extend(alph[:shift])
    cripto = ''
    for let in mes.lower():
        if let == ' ':
            cripto += ''.join(' ')
            continue
        tmp = alph.index(let)
        cripto += alph[tmp + shift]

    return cripto

message = 'Hello may friends'
k = 4

print(cripto_mes(message, alphabet_en, k))


# Другой вариант
# Шифрование случайным состоянием алфавита типа ключ шифрования :))
import random

def cripto_rand_mes(mes: str, alph: list) -> list:
    key_cript = []  # ключ шифрования :)
    alpha_bet = random.sample(alph, len(alph))  # случайное состояние алфавита

    for let in mes.lower():
        if let == ' ':
            key_cript.append(' ')
            continue
        tmp = alpha_bet.index(let)
        key_cript.append(tmp)

    return [key_cript, alpha_bet]


def de_cripto(key: list, alpha_sample: list) -> str:
    mes = ''
    for i in key:
        if i == ' ':
            mes += ''.join(' ')
            continue
        mes += alpha_sample[int(i)]

    return mes.capitalize()

message = 'Привет как дела'

keys = cripto_rand_mes(message, alphabet_ru)
print(*keys[0])

print(de_cripto(keys[0], keys[1]))
'''
Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ - значение переданного аргумента, а значение - имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
'''

import numbers


def key_params(**kwargs):
    result = {}
    for x, y in kwargs.items():
        if isinstance(y, numbers.Real) or (y is None):
            result[y] = x
        else:
            result[str(y)] = x

    return result


params = key_params(a=None, b='hello', c=[1, 2, 3], d={})
print(params)
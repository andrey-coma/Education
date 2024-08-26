"""
Задание 1. Поиск элемента
Пользователь вводит искомый ключ. Если он хочет, то может ввести
максимальную глубину — уровень, до которого будет просматриваться
структура.
Напишите функцию, которая находит заданный пользователем ключ в словаре
и выдаёт значение этого ключа на экран. По умолчанию уровень не задан. В
качестве примера можно использовать такой словарь:

site = {'html': {'head': {'title': 'Мой сайт'},
                 'body': {'h2': 'Здесь будет мой заголовок',
                          'div': 'Тут, наверное, какой-то блок',
                          'p': 'А вот здесь новый абзац'
                        }
                }
        }

Пример 1

Введите искомый ключ: head
Хотите ввести максимальную глубину? Y/N: n
Значение ключа: {'title': 'Мой сайт'}
Пример 2

Введите искомый ключ: head
Хотите ввести максимальную глубину? Y/N: y
Введите максимальную глубину: 1
Значение ключа: None

"""

site = {'html': {'head': {'title': 'Мой сайт'},
                 'body': {'h2': 'Здесь будет мой заголовок',
                          'div': 'Тут, наверное, какой-то блок',
                          'p': 'А вот здесь новый абзац'
                        }
                }
        }

res = None

def find_key(struct:dict, key:str, max_dept=None, dept=1) -> str:

    global res
    if (not max_dept is None) and (max_dept < dept):
        return res

    for keys, value in struct.items():
        if key == keys:
            return value
        if type(value) is dict:
            res = find_key(value, key, max_dept, dept=dept+1)

    return res

while True:
    f_key = input('Введите искомый ключ: ')
    if f_key.isalpha():
        answer = input('Хотите ввести максимальную глубину? Y/N: ')
        if answer.lower() == 'y':
            max_depth = input('Введите максимальную глубину: ')
            if max_depth.isdigit():
                max_depth = int(max_depth)
                break

        else:
            max_depth = None
            break

print(find_key(site, f_key, max_dept=max_depth, dept=1))
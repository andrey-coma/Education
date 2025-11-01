'''
Задание:
Напишите на C# или Python библиотеку для поставки внешним клиентам,
которая умеет вычислять площадь круга по радиусу и треугольника по трем сторонам.
Дополнительно к работоспособности оценим:
 - Юнит-тесты
 - Легкость добавления других фигур
 - Вычисление площади фигуры без знания типа фигуры в compile-time
 - Проверку на то, является ли треугольник прямоугольным
 '''


from math import pi, sqrt
import pprint

def square_circle(r:str) -> float:
    '''
    Функция производит расчет площади окружности
    :param r: радиус окружности
    :return: возвращает площадь окружности
    '''
    return round(pi * float(r) ** 2, 2)


def square_triangle(*args) -> tuple:
    '''
    Функция производит расчет площади треугольника
    :param args: стороны треугольника
    :return: возвращает площадь треугольника
    '''
    list_sides = [float(side) for side in args] # создадим список из сторон треугольника
    p = sum(list_sides) * 0.5 # найдем полупериметр
    s = sqrt(p * (p - list_sides[0]) * (p - list_sides[1]) * (p - list_sides[2])) # найдем площадь треугольника

    return round(s, 2), check_rectangular(*list_sides)


def check_rectangular(*args:float) -> str:
    '''
    Функция принимаем стороны треугольника и проверяет
    являться ли данный треугольник прямоугольным
    :param args: кортеж из сторон треугольника
    :return:
    '''
    numbers = sorted(args)
    #print(numbers)
    c = numbers.pop(-1)
    a, b = numbers[0], numbers[1]

    if c ** 2 == (a ** 2) + (b ** 2): # теорема Пифагора

        return f'треугольник является прямоугольным'

    return f'треугольник не является прямоугольным'


def check_numbers(*arg) -> bool:
    '''
    Функция пытается преобразовать строку в вещественное число
    :param arg: кортеж из строк
    :return: возвращает True при успехе и False при неудаче
    '''
    try:
        for num in arg:
            float(num)

        return True

    except ValueError as e:
        print('-' * 40)
        print('Введите целое или вещественное число!!!')
        print('-' * 40)

        return False


result = [] # список с результатами расчетов

while True:
    figure = input(f'Для вычисления площади окружности или треугольника введите '
                   f'радиус или стороны через пробел (для выхода N): ').split(' ')

    if figure[0].upper() == 'N':
        break

    if check_numbers(*figure):
        if len(figure) == 1:

            square_circle_dict = {
                'figure': 'circle',
                'radius': figure[0],
                'square': square_circle(*figure)
            }
            result.append(square_circle_dict)


        elif len(figure) == 3:

            square_triangle_dict = {
                'figure': 'triangle',
                'side_a': figure[0],
                'side_b': figure[1],
                'side_c': figure[2],
                'square': square_triangle(*figure)[0],
                'rectangular': square_triangle(*figure)[1]
            }
            result.append(square_triangle_dict)


        else:
            print(f'Фигуры с количеством сторон {len(figure)}, пока не реализованы...')


pprint.pprint(result, sort_dicts=False)
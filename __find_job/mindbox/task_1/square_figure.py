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

class SquareFigure:

    def __init__(self):
        pass

    # метод circle вычисляет площадь окружности
    def circle(self, r):
        if self.check_numbers(r):
            return round(pi * float(r) ** 2, 2)

        return None

    # метод circle вычисляет площадь треугольника
    def triangle(self, *args):
        if self.check_numbers(*args):
            list_sides = [float(side) for side in args]  # создадим список из сторон треугольника
            p = sum(list_sides) * 0.5  # найдем полупериметр
            s = sqrt(p * (p - list_sides[0]) * (p - list_sides[1]) * (p - list_sides[2]))  # найдем площадь треугольника

            return round(s, 2), self.check_rectangular(*list_sides)

        return None

    # метод check_rectangula проверяет, являться ли треугольник прямоугольным
    @staticmethod
    def check_rectangular(*args):
        numbers = sorted(args)
        c = numbers.pop(-1)
        a, b = numbers[0], numbers[1]

        if c ** 2 == (a ** 2) + (b ** 2):  # теорема Пифагора

            return f'является прямоугольным'

        return f'не является прямоугольным'

    # метод check_numbers пытается преобразовать строку в вещественное число
    @staticmethod
    def check_numbers(*arg):
        try:
            for num in arg:
                float(num)

            return True

        except ValueError as e:
            print('-' * 40)
            print('Введите целое или вещественное число!!!')
            print('-' * 40)

            return False

    # метод unknown_figure вычисляет площадь неизвестной фигуры по исходным данным
    def unknown_figure(self, *args):
        if self.check_numbers(*args):
            if len(args) == 1:
                return f'Площадь окружности {self.circle(*args)}'

            elif len(args) == 3:
                return f'Площадь треугольника {self.triangle(*args)}'

            return f'Фигуры с количеством сторон {len(args)}, пока не реализованы...'

        return None


# test
square = SquareFigure()
print(square.circle('25'))
print(square.triangle('25sd', 24, 7))
print(square.triangle('25', 24, 7))
print(square.unknown_figure(5))
print(square.unknown_figure(24, 25, 7))
print(square.unknown_figure(24, 25))
print(square.unknown_figure(24, 25, 6, 8))
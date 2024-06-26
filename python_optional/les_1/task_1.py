'''
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.

Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других,
то треугольника с такими сторонами не существует.

Отдельно сообщить является ли:
1 - треугольник разносторонним,
2 - равнобедренным или равносторонним,
только если треугольник существует .
'''


a = 5
b = 5
c = 7

if (a > b + c) | (b > c + a) | (c > a + b):
    print('Треугольник не существует')

elif (a != b) & (b != c) & (a != c):
    print('Треугольник существует')
    print('Треугольник разносторонний')

elif a == b | b == c:
    print('Треугольник существует')
    print('Треугольник равносторонний')

else:
    print('Треугольник существует')
    print('Треугольник равнобедренный')
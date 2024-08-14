"""
Задача Расстояние необязательная

Надо вычислить расстояние между 2 точками в пространстве любой размерности.
На входе два списка с координатами точек, на выходе одно число.
"""

points_one = [-1, 2, 4, 5]
points_two = [-5, 3, 6, 8]
result = []

for point in zip(points_one, points_two):
    result.append(point[0] + point[1])


print(sum(result))
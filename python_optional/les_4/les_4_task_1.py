# Напишите функцию для транспонирования матрицы transposed_matrix, 
# принимает в аргументы matrix, и возвращает транспонированную матрицу.

# matrix = [[1, 2, 6], [1, 3, 4]]

# 1 способ без функции zip


def transpose(matrix):
    if len(matrix) == 1:
        return matrix
    matrix_trans = []
    index = 0
    while index < len(matrix[1]):
        matrix_trans.append([])
        for i in matrix:
            matrix_trans[index].append(i[index])
        index += 1
    return matrix_trans


matrix_in = [[1, 2], [4, 5], [7, 8]]

print(transpose(matrix_in))


# 2 способ c zip


def transpose_zip(array):
    matrix_trans = []
    for i in zip(*array):
        matrix_trans.append([*i])
    return matrix_trans


print(transpose_zip(matrix_in))
#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy = matrix[:]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            copy[i][j] = matrix[i][j] ** 2
    return copy
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
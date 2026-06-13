#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[value ** 2 for value in row] for row in matrix]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)


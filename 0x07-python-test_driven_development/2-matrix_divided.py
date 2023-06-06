#!/usr/bin/python3

"""function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix)
            or not all(isinstance(item, (int, float))
                for item in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of \
                integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return ([list(map(lambda a: round(a / div, 2), row)) for row in matrix])

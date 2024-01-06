#!/usr/bin/python3
'''
Defines the matrix division function
'''


def matrix_divided(matrix, div):
    '''
    Divide the elements of a matrix
    elements in the matrix must be ints or floats
    the rows must also be equal
    '''
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(r, list) for r in matrix) or
            not all((isinstance(col, int) or isinstance(col, float))
                    for col in [n for r in matrix for n in r])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(r) == len(matrix[0]) for r in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), r)) for r in matrix])

#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_matrix = []
    for r in matrix:
        n_matrix.append([c ** 2 for c in r])
    return n_matrix

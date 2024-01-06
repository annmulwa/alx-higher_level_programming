#!/usr/bin/python3
'''
Defines a matrix multiplication function
'''


def matrix_mul(m_a, m_b):
    '''
    Multiplies two matrices.
    matrices shoould have the same sized rows
    they should contain either ints or floats
    they can't be empty
    '''

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(r, list) for r in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(r, list) for r in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(elem, int) or isinstance(elem, float))
               for elem in [n for r in m_a for n in r]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(elem, int) or isinstance(elem, float))
               for elem in [n for r in m_b for n in r]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(r) == len(m_a[0]) for r in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(r) == len(m_b[0]) for r in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    invert_b = []
    for row in range(len(m_b[0])):
        new_row = []
        for cnt in range(len(m_b)):
            new_row.append(m_b[cnt][row])
        invert_b.append(new_row)

    new_mat = []
    for r in m_a:
        new_row = []
        for c in invert_b:
            matr = 0
            for j in range(len(invert_b[0])):
                matr += r[j] * c[j]
            new_row.append(matr)
        new_mat.append(new_row)

    return new_mat

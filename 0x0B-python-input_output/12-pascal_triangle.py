#!/usr/bin/python3
'''
defines a function for the pascal
triangle
'''


def pascal_triangle(n):
    '''
    represents the pascal triangle
    '''
    if n <= 0:
        return []
    triangle = [[1]]
    while len(triangle) != n:
        tri_last = triangle [-1]
        tmp = [1]
        for i in range(len(tri_last) - 1):
            tmp.append(tri_last[i] + tri_last[i + 1])
        tmp.append(1)
        triangle.append(tmp)
    return triangle

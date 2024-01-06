#!/usr/bin/python3
'''
Defines a square function
'''


def print_square(size):
    '''
    prints a square using the # 
    size must be greater than 0
    size must be an int
    '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")

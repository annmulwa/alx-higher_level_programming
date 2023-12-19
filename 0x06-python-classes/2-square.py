#!/usr/bin/python3
'''square module'''


class Square:
    '''defines a square'''
    def __init__(self, size=0):
        '''size is a private instance attribute'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

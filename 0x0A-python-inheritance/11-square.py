#!/usr/bin/python3
'''
defines a square
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    square that inherits from rectangle
    '''
    def __init__(self, size):
        '''
        initializes the square
        '''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

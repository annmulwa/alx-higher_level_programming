#!/usr/bin/python3
'''
defines a class rectangle
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    inherits the basegeometry class
    '''
    def __init__(self, width, height):
        '''
        initialize a new rectangle with
        width and height
        '''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

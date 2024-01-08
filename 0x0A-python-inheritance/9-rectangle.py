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

    def area(self):
        '''
        area of the rectangle
        '''
        return self.__width * self.__height

    def __str__(self):
        '''
        string to return
        '''
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string

#!/usr/bin/python3
'''defines a rectangle class'''


class Rectangle:
    '''represents a rectangle'''
    def __init__(self, width=0, height=0):
        '''initializes the rectangle class'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''gets/sets the width of the rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''gets/sets the height of the rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''returns area of the rectangle'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''returns rectangle perimeter'''
        if (self.__width == 0 or self.__height == 0):
            return (0)
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        '''returns the printed rectangle using #'''
        if (self.__width == 0 or self.__height == 0):
            return ("")
        else:
            rec = []
            for i in range(self.__height):
                [rec.append('#') for j in range(self.__width)]
                if i != self.__height - 1:
                    rec.append('\n')
            return ("".join(rec))

    def __repr__(self):
        '''returns the string representation of the rectangle'''
        rec = "Rectangle (" + str(self.__width)
        rec += ", " + str(self.__height) + ")"
        return (rec)

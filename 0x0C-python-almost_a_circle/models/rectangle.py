#!/usr/bin/python3
'''
represents the class rectangle
that inherits from base
'''
from models.base import Base


class Rectangle(Base):
    '''
    represents the rectangle class
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Initializes the rectangle
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''
        set/get the width
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        sets the width
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''
        set/get the height
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        sets the height
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''
        set/get x
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        sets x
        '''
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''
        set/get y
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        sets y
        '''
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''
        returns the area of the rectangle
        '''
        return self.width * self.height

    def display(self):
        '''
        prints the rectangle with the
        character #
        '''
        for _ in range(self.y):
            print()

        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        '''
        returns a string of the attributes
        of the rectangle
        '''
        string = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width,
                                                         self.height)
        return string

    def update(self, *args, **kwargs):
        '''
        assigns arguments to attributes based
        on their position
        '''
        if args:
            arguments = ["id", "width", "height", "x", "y"]

            for i, attr in enumerate(arguments):
                if i < len(args):
                    setattr(self, attr, args[i])
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                else:
                    break

    def to_dictionary(self):
        '''
        returns the dictionary representation
        of a rectangle
        '''
        dic_rec = {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
        return dic_rec

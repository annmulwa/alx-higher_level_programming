#!/usr/bin/python3
'''
defines a class square that
inherits from a rectangle
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    represents a square class that inherits
    the rectangle class
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''
        initializes the square class
        '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''
        size getter
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''
        size setter
        '''
        self.width = value
        self.height = value

    def __str__(self):
        '''
        string representation of the square
        '''
        string = "[Square] ({}) {}/{} - {}".format(self.id,
                                                   self.x,
                                                   self.y,
                                                   self.width)
        return string

    def update(self, *args, **kwargs):
        '''
        assigns attributes according
        to index
        '''
        if args:
            for count, arg in enumerate(args):
                if count == 0:
                    self.id = arg
                elif count == 1:
                    self.size = arg
                elif count == 2:
                    self.x = arg
                elif count == 3:
                    self.y = arg
                else:
                    break
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                else:
                    break

    def to_dictionary(self):
        '''
        returns the dictionary representation
        of a square
        '''
        dic_square = {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
        return dic_square

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

    def __str__(self):
        '''
        string representation of the square
        '''
        string = "[Square] ({}) {}/{} - {}".format(self.id,
                                                   self.x,
                                                   self.y,
                                                   self.width)
        return string

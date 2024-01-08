#!/usr/bin/python3
'''
contains an empty class
'''


class BaseGeometry:
    '''
    BaseGeometry class
    '''
    def area(self):
        '''
        represents an area
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        name is always a string
        '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

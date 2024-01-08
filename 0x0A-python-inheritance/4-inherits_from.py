#!/usr/bin/python3
'''
checks if an object is an instance of
a class inherited from a class
'''


def inherits_from(obj, a_class):
    '''
    returns true if it is an instance
    otherwise false
    '''
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

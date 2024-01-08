#!/usr/bin/python3
'''
checks if an object is an instance of
the specified class
'''


def is_same_class(obj, a_class):
    '''
    returns true if an object is an instance
    of the specified class otherwise
    returns false
    '''
    if type(obj) == a_class:
        return True
    else:
        return False

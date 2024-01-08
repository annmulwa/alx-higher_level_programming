#!/usr/bin/python3
'''
checks if an onject is an instance of
the class or the inherited class
'''


def is_kind_of_class(obj, a_class):
    '''
    returns true if object is an instance
    otherwise false
    '''
    if isinstance(obj, a_class):
        return True
    return False

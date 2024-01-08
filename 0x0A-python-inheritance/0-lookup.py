#!/usr/bin/python3
'''
defines a function that returns a list of attributes
and available methods of an object
'''


def lookup(obj):
    '''
    returns a list of available attributes
    and methods
    '''
    return (dir(obj))

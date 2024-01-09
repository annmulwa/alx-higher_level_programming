#!/usr/bin/python3
'''
defines a function that returns the dictionary
description of a simple data structure for json
serialization of an object
'''


def class_to_json(obj):
    '''
    return sthe dictionary descpription of simple
    data for json serialization of an object
    '''
    return obj.__dict__

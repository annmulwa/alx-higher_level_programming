#!/usr/bin/python3
'''
Prints the first and last name
'''


def say_my_name(first_name, last_name=""):
    '''
    first name should be a string
    last name should also be a string
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

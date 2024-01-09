#!/usr/bin/python3
'''
defines a write function
'''


def write_file(filename="", text=""):
    '''
    writes a string to a text file
    and returns the number of chars
    written
    '''
    with open(filename, "w",  encoding="utf-8") as f:
        return f.write(text)

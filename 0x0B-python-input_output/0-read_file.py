#!/usr/bin/python3
'''
defines a function that reads
a textfile
'''


def read_file(filename=""):
    '''
    function that reads a text file
    '''
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

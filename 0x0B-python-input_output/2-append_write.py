#!/usr/bin/python3
'''
defines a function that appends a string to the
end of the text file
'''


def append_write(filename="", text=""):
    '''
    appends a string to the end of a text file and
    returns the number of chars
    '''
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

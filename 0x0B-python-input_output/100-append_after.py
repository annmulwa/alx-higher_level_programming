#!/usr/bin/python3
'''
defines a function to insert a text after a line
'''


def append_after(filename="", search_string="", new_string=""):
    '''
    inserts a text after a specific string
    '''
    text_insert = ""
    with open(filename) as f:
        for line in f:
            text_insert += line
            if search_string in line:
                text_insert += new_string
    with open(filename, "w") as fw:
        fw.write(text_insert)

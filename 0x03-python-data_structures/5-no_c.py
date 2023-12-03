#!/usr/bin/python3
def no_c(my_string):
    mynew_string = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            mynew_string += i
    return (mynew_string)

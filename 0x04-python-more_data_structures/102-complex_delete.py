#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    t = a_dictionary.copy()
    for k, v in t.items():
        if value == v:
            a_dictionary.pop(k)
    return a_dictionary

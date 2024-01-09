#!/usr/bin/python3
'''
function that writes an object to a text file
using JSON representation
'''
import json


def save_to_json_file(my_obj, filename):
    '''
    returns the json representation of an
    object after writing it
    '''
    with open(filename, "w") as f:
        json.dump(my_obj, f)

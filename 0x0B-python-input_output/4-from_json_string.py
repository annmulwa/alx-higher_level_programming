#!/usr/bin/python3
'''
function that returns the python
data structure of the JSON string
'''
import json


def from_json_string(my_str):
    '''
    returns an object which is the python data structure
    representation of the JSON string
    '''
    return json.loads(my_str)

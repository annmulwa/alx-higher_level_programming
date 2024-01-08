#!/usr/bin/python3
"""
function that adds new attributes to objects.
"""


def add_attribute(ob, at, val):
    """
    Add a new attribute to an object if possible
    ob - object to add an attribute to
    at - attribute to add to object
    val - value of attribute
    """
    if not hasattr(ob, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(ob, at, val)

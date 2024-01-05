#!/usr/bin/python3
'''defines a locked class'''


class LockedClass:
    '''
    allows the user to only create an instance
    attribute called first name
    '''
    __slots__ = ["first_name"]

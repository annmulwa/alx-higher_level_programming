#!/usr/bin/python3
'''
defines a class atudent
'''


class Student:
    '''
    Represents a student
    '''
    def __init__(self, first_name, last_name, age):
        '''
        Initializes a new student with
        public instance attributes
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        retrieves a dictionary representation of a
        student
        '''
        if (type(attrs) == list and
                all(type(elem) == str for elem in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        '''
        replaces all attributes of the student instance
        '''
        for k, v in json.items():
            setattr(self, k, v)

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

    def to_json(self):
        '''
        retrieves a dictionary representation of a
        student
        '''
        return self.__dict__

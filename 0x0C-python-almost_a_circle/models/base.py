#!/usr/bin/python3
'''
Represents the base class
'''
import json


class Base:
    '''
    The base class
    '''
    __nb_objects = 0
    def __init__(self, id=None):
        '''
        function to assign unique ids
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod        
    def to_json_string(list_dictionaries):
        '''
        returns the json representation of list
        dictionaries
        '''
        if list_dictionaries is None or list_dictionaries == []:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod    
    def save_to_file(cls, list_objs):
        '''
        writes the json resresentation of
        list_objs to a file
        '''
        filename = "{}.json".format(cls.__name__)
        
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dic = []
                for obj in list_objs:
                    list_dic.append(obj.to_dictionary())
                jsonfile.write(Base.to_json_string(list_dic))

    @staticmethod
    def from_json_string(json_string):
        '''
        returns a string from json representation
        to string
        '''
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
        returns an instance with all attributes
        already set
        '''
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        '''
        returns a list of instances
        '''
        filename = "{}.json".format(cls.__name__)
        
        try:
            with open(filename, "r") as jsonfile:
                list_dic = Base.from_json_string(jsonfile.read())
                list_inst = []

                for o in list_dic:
                    list_inst.append(cls.create(**o))
                return list_inst
        except FileNotFoundError:
                return []

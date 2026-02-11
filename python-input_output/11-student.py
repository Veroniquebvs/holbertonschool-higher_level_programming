#!/usr/bin/python3
"""
This module represents a student class
"""


class Student:
    """
    Define a student class
    """
    def __init__(self, first_name, last_name, age):
        """
        Instance of class student

        :param self: instance
        :param first_name: first name
        :param last_name: last name
        :param age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        This function returns a description of the object

        :param obj: object
        """
        descript_object = {}

        if attrs is not None:
            for i in attrs:
                if i in self.__dict__:
                    descript_object[i] = self.__dict__[i]
            return descript_object

        else:
            descript_object = self.__dict__
            return descript_object

    def reload_from_json(self, json):
        """
        This function replaces all attributes of the Student instance

        :param self: object
        :param json: dictionary
        """
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value

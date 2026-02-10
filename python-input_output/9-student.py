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

    def to_json(self):
        """
        This function returns a description of the object

        :param obj: object
        """
        descript_object = self.__dict__
        return descript_object

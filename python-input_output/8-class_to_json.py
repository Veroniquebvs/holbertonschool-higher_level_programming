#!/usr/bin/python3
"""
This module returns the dictionary description
"""


def class_to_json(obj):
    """
    This function returns a description of the object

    :param obj: object
    """
    descript_object = obj.__dict__
    return descript_object

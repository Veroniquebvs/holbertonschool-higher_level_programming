#!/usr/bin/python3
"""
This module checks whether an object
belongs to a specified class
"""


def is_same_class(obj, a_class):
    """
    This function returns True if the object is
    an instance of the specified class ; otherwise False.
    """
    if type(obj) is a_class:
        return True

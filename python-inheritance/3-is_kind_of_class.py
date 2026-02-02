#!/usr/bin/python3
"""
This module checks whether an object
belongs to a specified class or a class that inherited from
"""


def is_kind_of_class(obj, a_class):
    """
    This function returns True if the object is
    an instance of the specified class or a class that
    inherited from ; otherwise False.
    """

    return isinstance(obj, a_class)

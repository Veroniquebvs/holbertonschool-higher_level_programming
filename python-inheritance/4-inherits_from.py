#!/usr/bin/python3
"""
This module checks whether the object inherits
from the class, but is NOT the class itself
"""


def inherits_from(obj, a_class):
    """
    This function returns True if the object is
    an instance of the specified class or a class that
    inherited from ; otherwise False.
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class

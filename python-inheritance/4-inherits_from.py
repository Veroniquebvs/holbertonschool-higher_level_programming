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

    if type(obj) is a_class:
        return False
    if isinstance(obj, a_class):
        return True
    else:
        return False

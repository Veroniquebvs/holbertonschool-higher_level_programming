#!/usr/bin/python3
"""
This module checks whether an object inherits
from a specified class (but is not exactly that class)
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that
    inherits from a_class (directly or indirectly),
    but False if obj is exactly of type a_class
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)

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

    return isinstance(type(obj), a_class) and type(obj) is not a_class

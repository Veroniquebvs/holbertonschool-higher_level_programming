#!/usr/bin/python3

"""
This module print a list
"""


def lookup(obj):
    """
    This function returns the list of available
    attributes and methods of an object

    :param obj: Name of the object
    """
    print(list(obj.__dict__))

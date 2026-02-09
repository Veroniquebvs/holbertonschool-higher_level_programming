#!/usr/bin/python3
"""
This module returns the JSON representation of an object
"""


import json


def to_json_string(my_obj):
    """
    This function returns the JSON representation of an object

    :param my_obj: object
    """
    return json.dumps(my_obj)

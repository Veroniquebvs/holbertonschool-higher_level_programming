#!/usr/bin/python3
"""
This module returns an object represented by a JSON string
"""


import json


def from_json_string(my_str):
    """
    This function returns an object represented by a json string

    :param my_str: object
    """
    return json.loads(my_str)

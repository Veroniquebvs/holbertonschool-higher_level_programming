#!/usr/bin/python3
"""
This module creates an Object from a "JSON file"
"""

import json


def load_from_json_file(filename):
    """
    This function creates an Object from a "JSON file"

    :param filename: name of the file
    """
    with open(filename, "r") as f:
        return json.load(f)

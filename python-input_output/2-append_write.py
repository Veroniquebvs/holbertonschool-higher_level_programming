#!/usr/bin/python3
"""
This module adds a text at the end of the file
"""


def append_write(filename="", text=""):
    """
    This function appends a string at the end of a text file

    :param filename: name of the file
    :param text: text to add
    """
    with open(filename, "a") as f:
        return f.write(text)

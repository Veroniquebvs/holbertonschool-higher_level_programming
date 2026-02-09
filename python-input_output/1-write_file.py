#!/usr/bin/python3
"""
Module that writes a file
"""


def write_file(filename="", text=""):
    """
    Function that return number of characters

    filename : name of the file
    text : mode
    """
    with open(filename, "w") as f:
        return f.write(text)

#!/usr/bin/python3
"""
This module defines a function that reads a text file
"""


def read_file(filename=""):
    """
    Reads a text file and prints it to stdout
    """
    with open(filename, "r") as f:
        print(f.read(), end="")

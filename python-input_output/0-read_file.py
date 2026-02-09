#!/usr/bin/python3
"""
This module contain a function that reads a file
"""


def read_file(filename=""):
    """
    Reads a text file and prints it to stdout
    """
    with open(filename, "r") as f:
        contenu = f.read()
        print(contenu)

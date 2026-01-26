#!/usr/bin/python3
"""
This module defines a square.
"""


class Square:
    """
    This class defines a Square
    """
    def __init__(self, size=0):
        """
        This method define the size of the square
        size must be an integer
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

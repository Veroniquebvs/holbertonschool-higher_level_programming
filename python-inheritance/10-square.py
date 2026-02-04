#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle

"""
This module defines a square
"""


class Square(Rectangle):
    """
    This class defines a rectangle
    """

    def __init__(self, size):
        """
        This method initialize the object
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

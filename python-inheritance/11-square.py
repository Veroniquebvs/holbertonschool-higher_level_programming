#!/usr/bin/python3
"""
This module defines a square
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


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

    def __str__(self):
        """
        Returns the string representation of the square
        """
        return f"[Square] {self.__size}/{self.__size}"

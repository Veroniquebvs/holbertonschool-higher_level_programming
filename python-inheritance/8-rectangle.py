#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
This module defines a Rectangle
"""


class Rectangle(BaseGeometry):
    """
    This class defines a rectangle
    """
    def __init__(self, width, height):
        """
        This method initialize the object
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

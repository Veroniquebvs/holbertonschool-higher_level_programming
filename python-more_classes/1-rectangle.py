#!/usr/bin/python3
"""
This module defines a Rectangle class
"""


class Rectangle:
    """
    This class defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        This class defines a rectangle with width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        This method retrieves the widht of the rectangle
        """
        return self.__width

    @property
    def height(self):
        """
        This method retrives the position of the suqare
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        This method sets the width of a rectangle
        The width must be an integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        This method sets the height of a rectangle
        The height must be an integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

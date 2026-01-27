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
        self.__size = size

    @property
    def size(self):
        """
        This method retrieves the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This method sets the size of the square
        size must be an integer"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        This method define the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        This method prints a square with "#"
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)

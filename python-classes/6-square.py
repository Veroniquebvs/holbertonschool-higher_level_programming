#!/usr/bin/python3
"""
This module defines a square.
"""


class Square:
    """
    This class defines a Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        This method define the size of the square
        size must be an integer
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        This method retrieves the size of the square
        """
        return self.__size

    @property
    def position(self):
        """
        This method retrives the position of the suqare
        """
        return self.__position

    @size.setter
    def size(self, value):
        """
        This method sets the size of the square
        size must be an integer
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """
        This method sets the position of the square
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) and not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 and value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            if int(self.__position[1]) > 0:
                print("" * int(self.__position[1]))
            for i in range(self.__size):
                print(" " * int(self.__position[0]), end="")
                print("#" * self.__size)

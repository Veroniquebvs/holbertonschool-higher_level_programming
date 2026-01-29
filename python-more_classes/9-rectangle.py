#!/usr/bin/python3
"""
This module defines a Rectangle class
"""


class Rectangle:
    """
    This class defines a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        This class defines a rectangle with width and height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """
        This method print a message when an instance of rectangle is deleted
        """
        print(f"Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """
        This method retrieves the width of the rectangle
        """
        return self.__width

    @property
    def height(self):
        """
        This method retrives the height of the rectangle
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

    def area(self):
        """
        This function returns the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        This function returns the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            line = []
            for i in range(self.__height):
                line.append(str(self.print_symbol) * self.__width)
            return "\n".join(line)

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

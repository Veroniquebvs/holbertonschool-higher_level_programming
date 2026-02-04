#!/usr/bin/env python3
"""
This module defines abstract Shape class and
concrete Circle and Rectangles classes
"""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class for geometric shapes.

    Any subclass must implement the area and perimeter methods.
    """

    @abstractmethod
    def area(self):
        """
        Compute and return the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Compute and return the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Class representing a circle defined by its radius.
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Return the area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Return the perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Class representing a rectangle defined by its width and height.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """
        Return the area of the rectangle.
        """
        return self.height * self.width

    def perimeter(self):
        """
        Return the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape.

    This function relies on duck typing: any object that implements
    area() and perimeter() methods can be passed as an argument.
    """
    print(f"Area: {shape.area()}\nPerimeter: {shape.perimeter()}")

#!/usr/bin/env python3
"""
This module defines abstract Animal class and concrete Dog and Cat classes.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.

    This class cannot be instantiated directly and requires
    subclasses to implement the sound method.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that returns the sound of the animal.

        Returns:
            str: The sound made by the animal
        """
        pass


class Dog(Animal):
    """
    Concrete class representing a dog.

    Inherits from Animal and implements the sound method.
    """
    def sound(self):
        """
        Returns the sound a dog makes.

        Returns:
            str: "Bark"
        """
        return "Bark"


class Cat(Animal):
    """
    Concrete class representing a cat.

    Inherits from Animal and implements the sound method.
    """
    def sound(self):
        """
        Returns the sound a cat makes.

        Returns:
            str: "Meow"
        """
        return "Meow"

#!/usr/bin/python3
"""
Module that prints a square with the character #
"""


def print_square(size):
    """
    Prints a square of given size using the # character.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print_square(4)

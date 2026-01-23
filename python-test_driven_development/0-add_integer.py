#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Addition of two numbers

    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)

    return a+b


if __name__ == '__main__':
    import doctest
    0-add_integer()

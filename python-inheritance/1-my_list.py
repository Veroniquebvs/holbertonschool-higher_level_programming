#!/usr/bin/python3
"""
This module prints a list
"""


class MyList(list):
    """
    The class MyList inherits from the class list
    """
    def print_sorted(self):
        """
        This function prints a sorted list
        """
        new_list = sorted(self)
        print(new_list)

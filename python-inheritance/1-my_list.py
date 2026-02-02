#!/usr/bin/python3
"""
This module prints a list
"""


class MyList(list):
    def print_sorted(self):
        """
        This function prints a sorted list
        """
        new_list = sorted(self)
        print(new_list)

#!/usr/bin/python3
"""
This module defines MyList
"""


class MyList(list):
    def print_sorted(self):
        """
        Prints the list sorted in ascending order
        """
        new_list = list(self)
        new_list.sort()
        print(new_list)

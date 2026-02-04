#!/usr/bin/python3
"""
This module defines Mylist
"""


class MyList(list):
    def print_sorted(self):
        """
        This function prints a sorted list
        """
        new_list = self.copy()
        new_list.sort()
        print(new_list)

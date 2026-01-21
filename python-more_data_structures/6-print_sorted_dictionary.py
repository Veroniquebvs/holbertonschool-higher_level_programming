#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    new_list = dict(sorted(a_dictionary.items()))
    for i, j in new_list.items():
        print("{}: {}".format(i, j))

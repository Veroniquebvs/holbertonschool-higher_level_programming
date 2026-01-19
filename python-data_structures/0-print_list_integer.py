#!/usr/bin/python3

def print_list_integer(my_list=[]):
    str_my_list = str(my_list)

    for x in str_my_list:
        if x == "[" or x == "," or x == " " or x == "]":
            continue
        print("{}".format(x))

#!/usr/bin/python3

def no_c(my_string):
    i = 0
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        else:
            new_string = print("{}".format(i), end="")
    return new_string

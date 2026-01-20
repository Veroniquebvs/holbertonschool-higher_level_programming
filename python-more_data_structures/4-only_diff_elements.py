#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    new_set_1 = set()
    new_set_2 = set()
    for i in set_1:
        if i not in set_2:
            new_set_1.add(i)
    for j in set_2:
        if j not in set_1:
            new_set_2.add(j)

    new_set = new_set_1.union(new_set_2)
    return new_set

#!/usr/bin/python3

def roman_to_int(roman_string):
    dict_roman = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if not roman_string or not isinstance(roman_string, str):
        return 0

    result = 0
    for i in range(len(roman_string)):
        value = dict_roman[roman_string[i]]
        if i + 1 < len(roman_string) and (value <
                                          dict_roman[roman_string[i + 1]]):
            result -= value
        else:
            result += value
        return result

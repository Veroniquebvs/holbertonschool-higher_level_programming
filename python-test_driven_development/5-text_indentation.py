#!/usr/bin/python3
"""
Module that prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)
    result = ""

    while i < length:
        result += text[i]
        if text[i] in {'.', '?', ':'}:
            result += '\n\n'
            while i + 1 < length and text[i + 1] == ' ':
                i += 1
        i += 1

    print(result.strip())


if __name__ == "__main__":
    import doctest
    doctest.testmod()

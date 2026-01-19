#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence:
        new_tuple = (len(sentence), sentence[0])
        return new_tuple
    else:
        sentence[0] = None
        new_tuple = (len(sentence), sentence[0])

#!/usr/bin/env python3

class CountedIterator:
    def __init__(self, obj):
        self.it = iter(obj)
        self.count = 0

    def __next__(self):
        self.count += 1
        return next(self.it)

    def get_count(self):
        return self.count

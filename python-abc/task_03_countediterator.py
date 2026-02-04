#!/usr/bin/env python3

class CountedIterator:
    def __init__(self, obj):
        self.it = iter(obj)
        self.count = 0

    def __next__(self):
        item = next(self.it)
        self.count += 1
        return item

    def get_count(self):
        return self.count

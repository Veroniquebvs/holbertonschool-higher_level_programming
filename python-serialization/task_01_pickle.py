#!/usr/bin/env python3

import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        self.name = name

        if not isinstance(age, int):
            raise TypeError("age must be an integer")
        self.age = age

        if not isinstance(is_student, bool):
            raise TypeError("is_student must be an bool")
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except OSError:
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (EOFError, pickle.UnpicklingError):
            return None

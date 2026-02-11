#!/usr/bin/env python3

import json


def serialize_and_save_to_file(data, filename):
    # Your code here to serialize and save data to the specified file
    with open("data.json", "w") as filename:
        json.dump(data, filename)


def load_and_deserialize(filename):
    # Your code here to load and deserialize data from the specified file
    with open("data.json", "r") as filename:
        return json.load(filename)

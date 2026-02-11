#!/usr/bin/env python3

import csv
import json


def convert_csv_to_json(filename):
    csv_file = filename
    json_file = "data.json"
    data = []

    try:
        with open(csv_file, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
        with open(json_file, "w", encoding='utf-8') as f:
            json.dump(data, f)
        return True
    except FileNotFoundError:
        return False

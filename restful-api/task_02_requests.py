import requests
import json
import csv


def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == 200:
        print(f"Status Code: {r.status_code}")
        new_data = r.json()
        for item in new_data:
            print(item["title"])


def fetch_and_save_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    new_list = []
    if r.status_code == 200:
        new_data = r.json()
        for item in new_data:
            post_dict = {"id": item["id"], "title": item["title"],
                         "body": item["body"]}
            new_list.append(post_dict)

    csv_file = "posts.csv"
    with open(csv_file, "w", newline='', encoding='utf-8') as f:
        fieldnames = ["id", "title", "body"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(new_list)

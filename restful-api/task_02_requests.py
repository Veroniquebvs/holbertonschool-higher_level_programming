import requests
import json
import csv


def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    r.raise_for_status()
    print(f"Status Code: {r.status_code}")
    new_data = r.json()
    for item in new_data:
        print(item.get("title"))


def fetch_and_save_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    r.raise_for_status()
    new_data = r.json()
    post_dict = {}
    new_list = []
    for item in new_data:
        post_dict = {"id": item.get("id"), "title": item.get("title"),
                     "body": item.get("body")}
        new_list.append(post_dict)

    csv_file = "posts.csv"
    with open(csv_file, "w", newline='', encoding='utf-8') as f:
        fieldnames = new_list[0].keys()
        writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
        writer.writeheader()
        writer.writerows(new_list)

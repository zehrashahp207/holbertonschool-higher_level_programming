import requests
import csv

API_URL = 'https://jsonplaceholder.typicode.com/posts'


def fetch_and_print_posts():
    response = requests.get(API_URL)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))
    else:
        print("Failed to fetch posts.")


def fetch_and_save_posts():
    response = requests.get(API_URL)

    if response.status_code == 200:
        posts = response.json()
        formatted_posts = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]

        with open("posts.csv", "w", newline='', encoding='utf-8') as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(formatted_posts)
    else:
        print("Failed to fetch posts for saving.")
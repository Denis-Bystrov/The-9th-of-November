import json


def load_posts() -> list[dict]:
    with open("posts.json", "r", encoding="utf-8") as file:
        return json.load(file)


def post_by_word(word: str) -> list[dict]:
    result = []
    for post in load_posts():
        if word in post["content"]:
            result.append(post)
    return result


def add_post(post: dict) -> dict:
    posts: list[dict] = load_posts()
    posts.append(post)
    with open("posts.json", "w", encoding="utf-8") as file:
        json.dump(posts, file)
    return post

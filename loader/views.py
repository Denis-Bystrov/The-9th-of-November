import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request
from functions import add_post

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")


@loader_blueprint.route("/post")
def post_page():
    return render_template("post_form.html")


def save_picture(picture) -> str:
    filename = picture.filename
    path = f"uploads/images/{filename}"
    picture.save(path)
    return path


@loader_blueprint.route("/post", methods=["POST"])
def add_post_page():
    picture = request.files.get("picture")
    content = request.form.get("content")
    if not picture or not content:
        return "No data"
    if picture.filename.split(".")[-1] not in ["jpeg", "png"]:
        logging.info("Загруженный файл - не изображение")
        return "Изображение в недопустимом формате"

    try:
        picture_path: str = "/" + save_picture(picture)
    except FileNotFoundError:
        logging.error("К сожалению, данный файл не найден")
        return "К сожалению, данный файл не найден"
    except JSONDecodeError:
        return "Невалидный файл"
    post: dict = add_post({"pic": picture_path, "content": content})
    return render_template("post_uploaded.html", post=post)

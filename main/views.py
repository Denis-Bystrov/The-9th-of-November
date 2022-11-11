import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request
from functions import post_by_word

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")


@main_blueprint.route("/")
def main_page():
    return render_template("index.html")


@main_blueprint.route("/search/")
def search_page():
    search_result = request.args.get("s")
    logging.info("Выполняется поиск")
    try:
        posts = post_by_word(search_result)
    except FileNotFoundError:
        logging.error("К сожалению, данный файл не найден")
        return "К сожалению, данный файл не найден"
    except JSONDecodeError:
        return "Невалидный файл"
    return render_template("post_list.html", search_result=search_result, posts=posts)

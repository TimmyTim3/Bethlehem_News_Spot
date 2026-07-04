from flask import Blueprint, render_template

from services.article_service import get_all_articles

home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def index():
    articles = get_all_articles()

    return render_template(
        "index.html",
        articles=articles
    )

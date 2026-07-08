from flask import Blueprint, render_template

from services.article_service import (
    get_all_articles,
    get_featured_articles,
    get_breaking_articles,
    get_most_read_articles,
)

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def index():
    articles = get_all_articles()
    featured_articles = get_featured_articles()
    breaking_articles = get_breaking_articles()
    most_read_articles = get_most_read_articles()

    return render_template(
    "index.html",
    articles=articles,
    featured_articles=featured_articles,
    breaking_articles=breaking_articles,
    most_read_articles=most_read_articles,
)

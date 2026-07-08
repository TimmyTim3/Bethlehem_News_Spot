from flask import Blueprint, render_template

from services.article_service import (
    get_article_by_id,
    get_articles_by_category,
)
articles_bp = Blueprint(
    "articles",
    __name__
)


@articles_bp.route("/article/<int:article_id>")
def article(article_id):

    article = get_article_by_id(article_id)

    if article is None:
        abort(404)

    return render_template(
        "article.html",
        article=article
    )


@articles_bp.route("/category/<category>")
def category(category):
    articles = get_articles_by_category(category)

    return render_template(
        "category.html",
        category=category,
        articles=articles,
    )

from flask import Blueprint, render_template, abort

from services.article_service import get_article_by_id

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

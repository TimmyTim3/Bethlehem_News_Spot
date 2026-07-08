from flask import (
    Blueprint,
    render_template,
    request,
    abort,
)

from services.article_service import (
    get_article_by_id,
    get_articles_by_category,
    search_articles,
    increase_views,
)

articles_bp = Blueprint(
    "articles",
    __name__,
)


@articles_bp.route("/article/<int:article_id>")
def article(article_id):

    article = get_article_by_id(article_id)
    increase_views(article)

    if article is None:
        abort(404)

    increase_views(article)

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

@articles_bp.route("/search")
def search():

    search_term = request.args.get("q", "")

    articles = search_articles(search_term)

    return render_template(
        "search_results.html",
        search_term=search_term,
        articles=articles,
    )

from flask import (
    Blueprint,
    render_template,
    request,
    abort,
    jsonify,
)

from services.article_service import (
    get_article_by_id,
    get_articles_by_category,
    search_articles,
    increase_views,
    get_related_articles,
)

from models import db

articles_bp = Blueprint(
    "articles",
    __name__,
)


@articles_bp.route("/article/<int:article_id>")
def article(article_id):

    article = get_article_by_id(article_id)

    if article is None:
        abort(404)

    increase_views(article)

    related_articles = get_related_articles(article)

    return render_template(
        "article.html",
        article=article,
        related_articles=related_articles,
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

@articles_bp.route("/article/<int:article_id>/react", methods=["POST"])
def react(article_id):

    article = get_article_by_id(article_id)

    if article is None:
        return jsonify({"success": False})

    data = request.get_json()

    reaction = data.get("reaction")

    if reaction == "like":
        article.likes += 1

    elif reaction == "love":
        article.loves += 1

    elif reaction == "wow":
        article.wows += 1

    db.session.commit()

    return jsonify({
        "success": True,
        "likes": article.likes,
        "loves": article.loves,
        "wows": article.wows
    })

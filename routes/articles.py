from flask import (
    Blueprint,
    render_template,
    request,
    abort,
    jsonify,
    flash,
    redirect,
    url_for,
)

from models import db

from services.article_service import (
    get_article_by_id,
    get_articles_by_category,
    search_articles,
    increase_views,
    get_related_articles,
)

from services.comment_service import (
    get_comments_for_article,
    create_comment,
    like_comment,
)

from services.reaction_service import get_reactions

from services.moderation_service import (
    contains_profanity,
    is_spam,
)

articles_bp = Blueprint(
    "articles",
    __name__,
)


# ==========================
# VIEW ARTICLE
# ==========================

@articles_bp.route("/article/<int:article_id>")
def article(article_id):

    article = get_article_by_id(article_id)

    if article is None:
        abort(404)

    increase_views(article)

    related_articles = get_related_articles(article)

    comments = get_comments_for_article(article.id)

    reactions = get_reactions(article.category)

    return render_template(
        "article.html",
        article=article,
        related_articles=related_articles,
        comments=comments,
        reactions=reactions,
    )


# ==========================
# CATEGORY
# ==========================

@articles_bp.route("/category/<category>")
def category(category):

    articles = get_articles_by_category(category)

    return render_template(
        "category.html",
        category=category,
        articles=articles,
    )


# ==========================
# SEARCH
# ==========================

@articles_bp.route("/search")
def search():

    search_term = request.args.get("q", "")

    articles = search_articles(search_term)

    return render_template(
        "search_results.html",
        search_term=search_term,
        articles=articles,
    )


# ==========================
# REACTIONS
# ==========================

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
        "wows": article.wows,
    })


# ==========================
# COMMENTS
# ==========================

@articles_bp.route("/article/<int:article_id>/comment", methods=["POST"])
def add_comment(article_id):

    article = get_article_by_id(article_id)

    if article is None:
        abort(404)

    name = request.form.get("name")
    content = request.form.get("content")

    if name and content:

        if contains_profanity(content):

            flash(
                "Please keep discussions respectful.",
                "danger",
            )

            return redirect(
                url_for(
                    "articles.article",
                    article_id=article_id,
                )
            )

        if is_spam(content):

            flash(
                "Spam detected.",
                "danger",
            )

            return redirect(
                url_for(
                    "articles.article",
                    article_id=article_id,
                )
            )

        create_comment(
            article_id,
            name,
            content,
        )

    return redirect(
        url_for(
            "articles.article",
            article_id=article_id,
        )
    )


@articles_bp.route("/article/<int:article_id>/comment/<int:comment_id>/like", methods=["POST"])
def like_comment_route(article_id, comment_id):
    like_comment(comment_id)
    return redirect(url_for("articles.article", article_id=article_id))

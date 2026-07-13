from models import db
from models.comment import Comment


def get_comments_for_article(article_id):
    return (
        Comment.query
        .filter_by(article_id=article_id)
        .order_by(Comment.created_at.asc())
        .all()
    )


def create_comment(article_id, name, content):

    badge = "Community Member"

    previous_comments = (
        Comment.query
        .filter_by(name=name)
        .count()
    )

    if previous_comments >= 50:
        badge = "🏆 Local Legend"

    elif previous_comments >= 25:
        badge = "⭐ Top Contributor"

    elif previous_comments >= 10:
        badge = "🔥 Active Member"

    elif previous_comments >= 5:
        badge = "🌟 Regular Reader"

    elif previous_comments >= 1:
        badge = "💬 Returning Reader"

    comment = Comment(
        article_id=article_id,
        name=name,
        content=content,
        badge=badge,
    )

    db.session.add(comment)
    db.session.commit()

    return comment


def count_comments(article_id):
    return (
        Comment.query
        .filter_by(article_id=article_id)
        .count()
    )


def get_total_comments_by_user(name):
    return (
        Comment.query
        .filter_by(name=name)
        .count()
    )


def delete_comment(comment):
    db.session.delete(comment)
    db.session.commit()

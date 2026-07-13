from models import db
from models.comment import Comment


def get_comments_for_article(article_id):
    return (
        Comment.query
        .filter_by(article_id=article_id)
        .order_by(Comment.created_at.desc())
        .all()
    )


def create_comment(article_id, name, content):

    comment = Comment(
        article_id=article_id,
        name=name,
        content=content,
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


def delete_comment(comment):
    db.session.delete(comment)
    db.session.commit()

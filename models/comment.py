from datetime import datetime

from models import db


class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    article_id = db.Column(
        db.Integer,
        db.ForeignKey("articles.id"),
        nullable=False
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    content = db.Column(
        db.Text,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    # Profile expansion features
    avatar = db.Column(
        db.String(255),
        default="default-avatar.png"
    )

    badge = db.Column(
        db.String(50),
        default="Community Member"
    )

    # Phase 6.8.2: Like system
    likes = db.Column(
        db.Integer,
        default=0
    )

    article = db.relationship(
        "Article",
        backref=db.backref(
            "comments",
            lazy=True,
            cascade="all, delete-orphan"
        )
    )

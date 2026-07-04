from datetime import datetime
from models import db

class Article(db.Model):
    __tablename__ = "articles"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)

    summary = db.Column(db.String(500), nullable=False)

    content = db.Column(db.Text, nullable=False)

    category = db.Column(db.String(100), nullable=False)

    author = db.Column(db.String(100), nullable=False)

    image = db.Column(db.String(255))

    breaking = db.Column(db.Boolean, default=False)

    featured = db.Column(db.Boolean, default=False)

    views = db.Column(db.Integer, default=0)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

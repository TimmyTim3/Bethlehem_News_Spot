from datetime import datetime
from models import db

class Submission(db.Model):
    __tablename__ = "submissions"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(100),
        nullable=False
    )

    headline = db.Column(
        db.String(200),
        nullable=False
    )

    content = db.Column(
        db.Text,
        nullable=False
    )

    image = db.Column(
        db.String(255),
        nullable=True
    )

    # Status helps us manage the approval queue
    # 'pending', 'approved', 'rejected'
    status = db.Column(
        db.String(20),
        default="pending"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

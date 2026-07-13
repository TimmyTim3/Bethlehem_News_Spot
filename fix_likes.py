from app import app
from models import db
with app.app_context():
    db.session.execute(db.text("ALTER TABLE comments ADD COLUMN likes INTEGER DEFAULT 0"))
    db.session.commit()
    print("Added 'likes' column to database.")

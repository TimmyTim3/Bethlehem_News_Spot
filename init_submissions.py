from app import app
from models import db
from models.submission import Submission

with app.app_context():
    db.create_all()
    print("Submissions table created!")

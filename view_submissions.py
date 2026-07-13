from app import app
from models.submission import Submission

with app.app_context():
    submissions = Submission.query.all()
    if not submissions:
        print("The drawer is currently empty.")
    for s in submissions:
        print(f"ID: {s.id} | Headline: {s.headline} | Status: {s.status}")

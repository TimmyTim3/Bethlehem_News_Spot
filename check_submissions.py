from app import app
from models.submission import Submission

with app.app_context():
    all_subs = Submission.query.all()
    print(f"--- TOTAL SUBMISSIONS FOUND: {len(all_subs)} ---")
    for s in all_subs:
        print(f"ID: {s.id} | Headline: {s.headline} | Status: {s.status}")

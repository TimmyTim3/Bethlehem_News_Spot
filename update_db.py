from app import app
from models import db

with app.app_context():
    try:
        # Add the avatar column
        db.session.execute(db.text("ALTER TABLE comments ADD COLUMN avatar VARCHAR(255) DEFAULT 'default-avatar.png'"))
        db.session.commit()
        print("Successfully added 'avatar' column.")
    except Exception as e:
        print(f"Avatar column might already exist: {e}")

    try:
        # Add the badge column
        db.session.execute(db.text("ALTER TABLE comments ADD COLUMN badge VARCHAR(50) DEFAULT 'Community Member'"))
        db.session.commit()
        print("Successfully added 'badge' column.")
    except Exception as e:
        print(f"Badge column might already exist: {e}")

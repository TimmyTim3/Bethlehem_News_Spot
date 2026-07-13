from app import app
from models import db
from models.user import User

def create_admin():
    email = "admin@bethlehemnews.com" # Change this if you want
    password = "TimmyTim3"           # Change this immediately!

    with app.app_context():
        # Check if user already exists to avoid duplicates
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            print("Admin user already exists!")
            return

        # Create new admin
        admin = User(
            username="admin",
            email=email,
            role="admin"
        )
        admin.set_password(password)
        
        db.session.add(admin)
        db.session.commit()
        print(f"Admin user '{email}' created successfully!")

if __name__ == "__main__":
    create_admin()

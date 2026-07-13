from app import app
from models import db
from models.user import User

with app.app_context():
    db.create_all()
    print("Users table created!")

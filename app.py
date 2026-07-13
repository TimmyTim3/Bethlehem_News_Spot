import os
from flask import Flask
from flask_login import LoginManager
from models import db
from models.user import User  # Import User
from config import Config

# Initialize App
app = Flask(__name__)
app.config.from_object(Config)

# Initialize Database
db.init_app(app)

# Initialize Login Manager (The Gatekeeper)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Register Blueprints
from routes.home import home_bp
from routes.articles import articles_bp
from routes.admin import admin_bp
from routes.submissions import submissions_bp
from routes.auth import auth_bp  # Import new auth route

app.register_blueprint(home_bp)
app.register_blueprint(articles_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(submissions_bp)
app.register_blueprint(auth_bp)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)

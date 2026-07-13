from routes.submissions import submissions_bp
from models.comment import Comment
from routes.admin import admin_bp
from flask import Flask
from config import Config
from models import db
from routes.home import home_bp
from routes.articles import articles_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(admin_bp)

app.register_blueprint(home_bp)

app.register_blueprint(articles_bp)

app.register_blueprint(submissions_bp)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)

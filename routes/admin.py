import os
from models.comment import Comment
from services.comment_service import delete_comment
from werkzeug.utils import secure_filename
from flask import current_app
from flask import Blueprint, render_template, redirect, url_for
from forms.article_form import ArticleForm
from services.article_service import (
    create_article,
    get_all_articles_admin,
)

admin_bp = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin"
)

@admin_bp.route("/comments")
def comments():

    comments = (
        Comment.query
        .order_by(Comment.created_at.desc())
        .all()
    )

    return render_template(
        "admin/comments.html",
        comments=comments,
    )

@admin_bp.route("/new", methods=["GET", "POST"])
def new_article():

    form = ArticleForm()

    filename = None

    if form.image.data:

        image = form.image.data

        filename = secure_filename(image.filename)

        image.save(
            os.path.join(
                current_app.config["UPLOAD_FOLDER"],
                filename,
            )
        )

    if form.validate_on_submit():
        create_article(form, filename)
        return redirect(url_for("home.index"))

    return render_template(
        "admin/new_article.html",
        form=form
    )

@admin_bp.route("/")
def dashboard():
    return render_template("admin/dashboard.html")

@admin_bp.route("/articles")
def list_articles():

    articles = get_all_articles_admin()

    return render_template(
        "admin/articles.html",
        articles=articles
    )

import os
from models.comment import Comment
from models.article import Article
from models import db
from services.comment_service import delete_comment
from werkzeug.utils import secure_filename
from flask import current_app, request, flash, Blueprint, render_template, redirect, url_for
from flask_login import login_required  # Added this
from forms.article_form import ArticleForm
from services.article_service import (
    create_article,
    get_all_articles_admin,
)
from services.submission_service import (
    get_pending_submissions,
    get_submission_by_id,
    reject_submission,
)

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.route("/comments")
@login_required  # Locked
def comments():
    comments = Comment.query.order_by(Comment.created_at.desc()).all()
    return render_template("admin/comments.html", comments=comments)

@admin_bp.route("/submissions")
@login_required  # Locked
def submissions():
    pending_submissions = get_pending_submissions()
    return render_template("admin/submissions.html", submissions=pending_submissions)

@admin_bp.route("/submissions/<int:submission_id>/edit", methods=["GET", "POST"])
@login_required  # Locked
def edit_submission_route(submission_id):
    sub = get_submission_by_id(submission_id)
    if not sub: return redirect(url_for("admin.submissions"))
    
    if request.method == "POST":
        sub.headline = request.form.get("headline")
        sub.content = request.form.get("content")
        db.session.commit()
        flash("Submission updated successfully!", "success")
        return redirect(url_for("admin.submissions"))
        
    return render_template("admin/edit_submission.html", submission=sub)

@admin_bp.route("/submissions/<int:submission_id>/approve", methods=["POST"])
@login_required  # Locked
def approve_submission_route(submission_id):
    sub = get_submission_by_id(submission_id)
    if sub:
        new_article = Article(
            title=sub.headline,
            summary=sub.content[:100] + "...",
            content=sub.content,
            category="Community",
            author="Community",
            published=True
        )
        db.session.add(new_article)
        db.session.delete(sub)
        db.session.commit()
        flash("Submission promoted to article!", "success")
    return redirect(url_for("admin.submissions"))

@admin_bp.route("/submissions/<int:submission_id>/reject", methods=["POST"])
@login_required  # Locked
def reject_submission_route(submission_id):
    sub = get_submission_by_id(submission_id)
    if sub:
        reject_submission(sub)
        flash("Submission rejected.", "info")
    return redirect(url_for("admin.submissions"))

@admin_bp.route("/new", methods=["GET", "POST"])
@login_required  # Locked
def new_article():
    form = ArticleForm()
    filename = None
    if form.image.data:
        image = form.image.data
        filename = secure_filename(image.filename)
        image.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))
    if form.validate_on_submit():
        create_article(form, filename)
        return redirect(url_for("home.index"))
    return render_template("admin/new_article.html", form=form)

@admin_bp.route("/")
@login_required  # Locked
def dashboard():
    return render_template("admin/dashboard.html")

@admin_bp.route("/articles")
@login_required  # Locked
def list_articles():
    articles = get_all_articles_admin()
    return render_template("admin/articles.html", articles=articles)

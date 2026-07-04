from services.article_service import (
    create_article,
    get_article_by_id,
    update_article,
    delete_article,
)
from flask import redirect, url_for
from services.article_service import create_article
from forms.article_form import ArticleForm
from flask import Blueprint, render_template

admin_bp = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin"
)

@admin_bp.route("/delete/<int:article_id>", methods=["POST"])
def delete_article_route(article_id):
    article = get_article_by_id(article_id)

    if article is None:
        abort(404)

    delete_article(article)

    return redirect(url_for("home.index"))

@admin_bp.route("/new", methods=["GET", "POST"])
def new_article():
    form = ArticleForm()

    if form.validate_on_submit():
        create_article(form)
        return redirect(url_for("home.index"))

    return render_template(
        "admin/new_article.html",
        form=form
    )

@admin_bp.route("/")
def dashboard():
    return render_template("admin/dashboard.html")

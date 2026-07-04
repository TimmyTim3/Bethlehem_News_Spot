from forms.article_form import ArticleForm
from flask import Blueprint, render_template

admin_bp = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin"
)

@admin_bp.route("/new", methods=["GET"])
def new_article():

    form = ArticleForm()

    return render_template(
        "admin/new_article.html",
        form=form
    )

@admin_bp.route("/")
def dashboard():
    return render_template("admin/dashboard.html")

from flask import (
    Blueprint,
    render_template,
    request,
)

from models.article import Article

from services.article_service import (
    get_all_articles,
    get_featured_articles,
    get_breaking_articles,
    get_most_read_articles,
)

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def index():
    page = request.args.get("page", 1, type=int)

    articles = get_all_articles(page=page)
    featured_articles = get_featured_articles()
    side_articles = (
    Article.query
    .filter_by(published=True)
    .order_by(Article.id.desc())
    .limit(3)
    .all()
)
    breaking_articles = get_breaking_articles()
    most_read_articles = get_most_read_articles()

    return render_template(
        "index.html",
        articles=articles,
        featured_articles=featured_articles,
        side_articles=side_articles,
        breaking_articles=breaking_articles,
        most_read_articles=most_read_articles,
    )


from models.article import Article

def get_article_by_id(article_id):
    return Article.query.get(article_id)


def get_all_articles():
    return Article.query.order_by(Article.created_at.desc()).all()


def get_featured_articles():
    return (
        Article.query.filter_by(featured=True)
        .order_by(Article.created_at.desc())
        .all()
    )


def get_breaking_articles():
    return (
        Article.query.filter_by(breaking=True)
        .order_by(Article.created_at.desc())
        .all()
    )

from models import db
from models.article import Article


def create_article(form):
    article = Article(
        title=form.title.data,
        summary=form.summary.data,
        content=form.content.data,
        category=form.category.data,
        author=form.author.data,
        breaking=form.breaking.data,
        featured=form.featured.data,
    )

    db.session.add(article)
    db.session.commit()

    return article

def update_article(article, form):
    article.title = form.title.data
    article.summary = form.summary.data
    article.content = form.content.data
    article.category = form.category.data
    article.author = form.author.data
    article.breaking = form.breaking.data
    article.featured = form.featured.data

    db.session.commit()

    return article

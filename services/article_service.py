from sqlalchemy import or_
from models import db
from models.article import Article


# -------------------------
# READ
# -------------------------

def search_articles(search_term):
    return (
        Article.query.filter(
            or_(
                Article.title.ilike(f"%{search_term}%"),
                Article.summary.ilike(f"%{search_term}%"),
                Article.content.ilike(f"%{search_term}%"),
                Article.category.ilike(f"%{search_term}%"),
                Article.author.ilike(f"%{search_term}%"),
            )
        )
        .order_by(Article.created_at.desc())
        .all()
    )


def get_all_articles():
    return Article.query.order_by(Article.created_at.desc()).all()


def get_all_articles_admin():
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


def get_article_by_id(article_id):
    return db.session.get(Article, article_id)


def get_articles_by_category(category):
    return (
        Article.query
        .filter_by(category=category)
        .order_by(Article.created_at.desc())
        .all()
    )

# -------------------------
# CREATE
# -------------------------

def create_article(form, filename=None):
    article = Article(
        title=form.title.data,
        image=filename,
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


# -------------------------
# UPDATE
# -------------------------

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


# -------------------------
# DELETE
# -------------------------

def delete_article(article):
    db.session.delete(article)
    db.session.commit()

def increase_views(article):

    article.views += 1

    db.session.commit()

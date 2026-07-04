from models.article import Article


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

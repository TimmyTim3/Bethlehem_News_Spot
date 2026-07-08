from app import app
from models import db
from models.article import Article

from seed_data.articles import ARTICLES


with app.app_context():

    print("Deleting old articles...")

    Article.query.delete()

    db.session.commit()

    print("Adding new articles...")

    for item in ARTICLES:

        article = Article(

            title=item["title"],
            summary=item["summary"],
            content=item["content"],
            author=item["author"],
            category=item["category"],
            breaking=item["breaking"],
            featured=item["featured"],
            published=item["published"],
            views=item["views"],
            image=item["image"],

        )

        db.session.add(article)

    db.session.commit()

    print("Done!")

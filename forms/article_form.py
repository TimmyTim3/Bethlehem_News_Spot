from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextAreaField,
    BooleanField,
    SubmitField,
)
from wtforms.validators import DataRequired


class ArticleForm(FlaskForm):
    title = StringField(
        "Headline",
        validators=[DataRequired()]
    )

    summary = TextAreaField(
        "Summary",
        validators=[DataRequired()]
    )

    content = TextAreaField(
        "Content",
        validators=[DataRequired()]
    )

    category = StringField(
        "Category",
        validators=[DataRequired()]
    )

    author = StringField(
        "Author",
        validators=[DataRequired()]
    )

    breaking = BooleanField("Breaking News")

    featured = BooleanField("Featured")

    submit = SubmitField("Publish")

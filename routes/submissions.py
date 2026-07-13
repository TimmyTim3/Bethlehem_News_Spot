from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
)
from services.submission_service import create_submission

submissions_bp = Blueprint("submissions", __name__)

@submissions_bp.route("/submit-news", methods=["GET", "POST"])
def submit_news():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        headline = request.form.get("headline")
        content = request.form.get("content")

        if name and email and headline and content:
            create_submission(name, email, headline, content)
            flash("Thank you! Your story has been submitted for review.", "success")
            return redirect(url_for("submissions.submit_news"))
        else:
            flash("Please fill in all fields.", "danger")

    return render_template("submit_news.html")

from models import db
from models.submission import Submission


def create_submission(name, email, headline, content, image=None):
    """
    Creates a new community submission and stores it as 'pending'.
    """
    submission = Submission(
        name=name,
        email=email,
        headline=headline,
        content=content,
        image=image,
        status="pending"
    )

    db.session.add(submission)
    db.session.commit()

    return submission


def get_pending_submissions():
    """
    Retrieves all submissions that haven't been reviewed yet.
    """
    return Submission.query.filter_by(status="pending").order_by(Submission.created_at.desc()).all()


def get_submission_by_id(submission_id):
    """
    Gets a single submission by its ID for review.
    """
    return Submission.query.get(submission_id)


def approve_submission(submission):
    """
    Updates the status to approved. 
    (We will use this later when we promote a submission to an actual Article).
    """
    submission.status = "approved"
    db.session.commit()


def reject_submission(submission):
    """
    Updates the status to rejected.
    """
    submission.status = "rejected"
    db.session.commit()


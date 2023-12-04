from flask import Blueprint
from flask import Flask, render_template ,jsonify, make_response, redirect, request, url_for, session
from exts import db
from models import UserModel, GithubModel,CollectModel,RatingModel

bp = Blueprint("profile", __name__, url_prefix="/profile")

@bp.route("/")
def profile():
    user_id=session['user_id']
    # print(user_id)
    collects = CollectModel.query.filter_by(userId=user_id).all()
    github_details = []
    for item in collects:
        github_id = item.githubId
        github = GithubModel.query.get(github_id)
        github_details.append(github)
    # print(github_details)

    ratings = RatingModel.query.filter_by(userId=user_id).all()
    rating_details = []
    for item in ratings:
        github_id = item.githubId
        github = GithubModel.query.get(github_id)
        # rating_details.append(github)
        rating_details.append({"name":github.name, "introduction":github.introduction, "githubId":github_id, "rating":item.rating})
    return render_template("profile.html",userId=user_id,collects=github_details,ratings=rating_details)

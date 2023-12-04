from flask import Blueprint
from flask import Flask, render_template ,jsonify, make_response, redirect, request, url_for, session
from exts import db
from models import GithubModel, RatingModel, CollectModel
import time


bp = Blueprint("content", __name__, url_prefix="/content")


@bp.route("/")
def content():
    id = request.args.get("id")
    github = GithubModel.query.filter_by(id=id).first()

    githubId = id
    userId = session['user_id']
    rating = RatingModel.query.filter_by(userId=userId,githubId=githubId).first()
    collect = CollectModel.query.filter_by(userId=userId,githubId=githubId).first()
    is_collect = 0
    myrating = 0
    if rating:
        myrating = rating.rating
    if collect:
        is_collect = 1
    return render_template("content.html", github = github, rating = myrating, is_collect = is_collect)


@bp.route("/star", methods=['POST'])
def star():
    content = request.get_json('content')
    githubId = content['githubId']
    userId = session['user_id']
    new_rating = content['rating']
    timestamp = int(time.time())

    old_rating_data = RatingModel.query.filter_by(userId=userId,githubId=githubId).first()
    if old_rating_data:
        old_rating_data.rating = float(new_rating)
        old_rating_data.timestamp = timestamp
        db.session.commit()
    else:
        new_rating_data = RatingModel(userId=userId,githubId=githubId,rating=new_rating,timestamp=timestamp)
        db.session.add(new_rating_data)
        db.session.commit()
    return "success"


@bp.route("/collect", methods=['POST'])
def collect():
    content = request.get_json('content')
    new_is_collect = content['is_collect']
    userId = session['user_id']
    githubId = content['githubId']

    print("传入函数中的new_is_collect: ", new_is_collect)

    if new_is_collect == 1:
        new_collect_data = CollectModel(userId=userId,githubId=githubId)
        db.session.add(new_collect_data)
        db.session.commit()
    else:
        CollectModel.query.filter(CollectModel.userId == userId, CollectModel.githubId == githubId).delete()
        db.session.commit()
    return "success"
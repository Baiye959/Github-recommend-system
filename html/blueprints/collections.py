from flask import Blueprint
from flask import Flask, render_template ,jsonify, make_response, redirect, request, url_for, session
from exts import db
from models import UserModel, GithubModel

bp = Blueprint("collections", __name__, url_prefix="/collections")

@bp.route("/")
def collections():
    language = request.args.get("language")
    if language:
        githubs = GithubModel.query.filter_by(language=language).all()
        return render_template("collections.html", githubs = githubs)
    else:
        return render_template("collections.html", githubs = [])
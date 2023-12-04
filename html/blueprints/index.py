from flask import Blueprint
from flask import Flask, render_template ,jsonify, make_response, redirect, request, url_for, session
from exts import db
from models import UserModel, GithubModel

bp = Blueprint("index", __name__, url_prefix="/")

@bp.route("/")
def index():
    items_github = GithubModel.query.order_by(GithubModel.id.desc()).limit(10).all()
    return render_template("index.html",items_github=items_github)

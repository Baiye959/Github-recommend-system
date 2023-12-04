from flask import Blueprint
from flask import Flask, render_template ,jsonify, make_response, redirect, request, url_for, session
from .forms import RegisterForm, LoginForm
from exts import db
from models import UserModel
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/")
def auth():
    return render_template("auth.html")

@bp.route("/login", methods=['POST'])
def login():
    form = LoginForm(request.form)
    if form.validate():
        email = form.email.data
        password = form.password.data
        user = UserModel.query.filter_by(email=email).first()
        if not user:
            print("邮箱在数据库中不存在")
            return redirect("/auth")
        if check_password_hash(user.password, password):
            # cookie
            session['user_id'] = user.id
            return redirect("/")
        else:
            print("密码错误")
            return redirect("/auth")
    else:
        print(form.errors)
        return redirect("/auth")

@bp.route("/register", methods=['POST'])
def register():
    form = RegisterForm(request.form)
    if form.validate():
        email = form.email.data
        username = form.username.data
        password = form.password.data
        user = UserModel(email=email,username=username,password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        return redirect("/auth")
    else:
        print(form.errors)
        return redirect("/auth")

@bp.route("/logout")
def logout():
    session.clear()
    return redirect("/auth")
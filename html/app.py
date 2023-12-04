from flask import Flask, render_template, jsonify, make_response, session, g
from gevent import pywsgi # pywsgi: flask开发环境转生产环境
import config
from sqlalchemy import text
from exts import db
from models import UserModel
from blueprints.auth import bp as auth_bp
from blueprints.collections import bp as collections_bp
from blueprints.content import bp as content_bp
from blueprints.profile import bp as profile_bp
from blueprints.index import bp as index_bp


app = Flask(__name__)
# 绑定配置文件
app.config.from_object(config)

db.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(collections_bp)
app.register_blueprint(content_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(index_bp)

@app.before_request
def my_before_request():
    user_id = session.get("user_id")
    if user_id:
        user = UserModel.query.get(user_id)
        setattr(g, "user", user)
    else:
        setattr(g, "user", None)

@app.context_processor
def my_context_processor():
    return {"user": g.user}


if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
    server.serve_forever()
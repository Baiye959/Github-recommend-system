from exts import db

class UserModel(db.Model):
    __tablename__="user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # varchar,null=0
    username = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(200),nullable=False)
    email = db.Column(db.String(100),nullable=False)

class GithubModel(db.Model):
    __tablename__="github_info"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # varchar,null=0
    name = db.Column(db.String(1000),nullable=False)
    link = db.Column(db.String(1000),nullable=False)
    introduction = db.Column(db.String(5000),nullable=False)
    language = db.Column(db.String(64),nullable=False)
    stars = db.Column(db.Integer,nullable=False)
    forks = db.Column(db.Integer,nullable=False)

class RatingModel(db.Model):
    __tablename__="ratings"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # varchar,null=0
    userId = db.Column(db.Integer,nullable=False)
    githubId = db.Column(db.Integer,nullable=False)
    rating = db.Column(db.Float,nullable=False)
    timestamp = db.Column(db.Integer,nullable=False)

class CollectModel(db.Model):
    __tablename__="collect"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # varchar,null=0
    githubId = db.Column(db.Integer,nullable=False)
    userId = db.Column(db.Integer,nullable=False)

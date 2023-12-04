class User(db.Model):
    __tablename_="user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # varchar,null=0
    username = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(200),nullable=False)
    email = db.Column(db.String(100),nullable=False)

from db import db


class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(32))

    def __init__(self, username, password):
        self.username = username
        self.password = password

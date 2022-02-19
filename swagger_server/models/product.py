from db import db


class Product(db.Model):

    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(2, asdecimal=True))

    def __init__(self, name, price):
        self.name = name
        self.price = price

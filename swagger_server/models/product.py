from db import db
from base_model_ import Model


class Product(Model):

    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(2, asdecimal=True))
    product_categories = db.relationship(
        "ProductCategory", back_populates="product")

    def __init__(self, name, price):
        self.name = name
        self.price = price

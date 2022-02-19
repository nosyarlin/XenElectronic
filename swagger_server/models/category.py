from db import db
from base_model_ import Model


class Category(Model):

    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    product_categories = db.relationship(
        "ProductCategory", back_populates="product")

    def __init__(self, name):
        self.name = name

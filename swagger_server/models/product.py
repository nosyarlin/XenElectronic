from db import db
from models.product_category import ProductCategory
from models.category import Category


class Product(db.Model):

    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(2, asdecimal=True))

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def filter_by_category(cls, category):
        return cls.query\
            .join(ProductCategory)\
            .join(Category)\
            .filter_by(category=category)\
            .all()

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

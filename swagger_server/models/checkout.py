from db import db
from base_model_ import Model


class Checkout(Model):

    __tablename__ = 'checkout'

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates="checkouts")
    checkoutProducts = db.relationship(
        'CheckoutProduct', back_populates="checkout")

    def __init__(self, name, price):
        self.name = name
        self.price = price

from db import db
from base_model_ import Model


class CheckoutProduct(Model):

    __tablename__ = 'checkout_product'

    id = db.Column(db.Integer, primary_key=True)
    checkoutId = db.Column(db.Integer, db.ForeignKey('checkout.id'))
    checkout = db.relationship("Checkout", back_populates="checkoutProducts")
    productId = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship('Product')
    quantity = db.Column(db.Integer)

    def __init__(self, checkoutId, productId, quantity):
        self.checkoutId = checkoutId
        self.productId = productId
        self.quantity = quantity

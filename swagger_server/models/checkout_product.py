from db import db


class CheckoutProduct(db.Model):

    __tablename__ = 'checkout_product'

    id = db.Column(db.Integer, primary_key=True)
    checkoutId = db.Column(db.Integer, db.ForeignKey('checkout.id'))
    productId = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer)

    def __init__(self, checkoutId, productId, quantity):
        self.checkoutId = checkoutId
        self.productId = productId
        self.quantity = quantity

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

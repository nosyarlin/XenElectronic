from db import db
from base_model_ import Model


class ProductCategory(Model):

    __tablename__ = 'product_category'

    id = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship("Product", back_populates="product_categories")
    categoryId = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship("Category", back_populates="product_categories")
    quantity = db.Column(db.Integer)

    def __init__(self, checkoutId, productId, quantity):
        self.checkoutId = checkoutId
        self.productId = productId
        self.quantity = quantity

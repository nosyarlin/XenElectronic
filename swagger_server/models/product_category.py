from db import db
from base_model_ import Model


class ProductCategory(Model):

    __tablename__ = 'product_category'

    id = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship("Product", back_populates="product_categories")
    categoryId = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship("Category", back_populates="product_categories")

    def __init__(self, productId, categoryId):
        self.productId = productId
        self.categoryId = categoryId

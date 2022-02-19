from db import db


class ProductCategory(db.Model):

    __tablename__ = 'product_category'

    id = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.Integer, db.ForeignKey('product.id'))
    categoryId = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __init__(self, productId, categoryId):
        self.productId = productId
        self.categoryId = categoryId

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

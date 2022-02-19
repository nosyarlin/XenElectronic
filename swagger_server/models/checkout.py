from db import db


class Checkout(db.Model):

    __tablename__ = 'checkout'

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, userId):
        self.userId = userId

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def json(self):
        return {
            'id': self.id,
            'userId': self.userId
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

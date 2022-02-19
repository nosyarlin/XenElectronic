#!/usr/bin/env python3

from flask import Flask
from flask_restful import Api
from resources.product import ProductResource
from resources.checkout import CheckoutResource


def create_app(db):
    app = Flask(__name__)
    app.app_context().push()

    # Setup db
    db.init_app(app)
    db.create_all()

    # Setup API
    api = Api(app)
    api.add_resource(ProductResource, '/product')
    api.add_resource(CheckoutResource, '/checkout', '/checkout/<id>')
    return app


if __name__ == '__main__':
    from db import db
    app = create_app(db)
    app.run(port=5000, debug=True)

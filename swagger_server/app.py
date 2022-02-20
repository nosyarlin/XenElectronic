#!/usr/bin/env python3

from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from resources.product import ProductResource
from resources.checkout import CheckoutResource
from resources.user import UserResource
from utils import create_test_data


def create_app():

    from db import db

    app = Flask(__name__)
    CORS(app)
    app.app_context().push()

    # Setup db
    db.init_app(app)
    db.create_all()
    create_test_data()

    # Setup API
    api = Api(app)
    api.add_resource(ProductResource, '/search')
    api.add_resource(CheckoutResource, '/checkout', '/checkout/<id>')
    api.add_resource(UserResource, '/login')
    return app


def main():
    app = create_app()
    app.run(port=5000, debug=True)


if __name__ == '__main__':
    main()

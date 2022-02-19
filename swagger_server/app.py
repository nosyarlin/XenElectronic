#!/usr/bin/env python3

from flask import Flask


def create_app(db):
    app = Flask(__name__)
    app.app_context().push()
    db.init_app(app)
    db.create_all()
    return app


if __name__ == '__main__':
    from db import db
    app = create_app(db)
    app.run(port=5000, debug=True)

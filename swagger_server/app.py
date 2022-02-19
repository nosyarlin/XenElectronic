#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    from db import db
    app.app_context().push()
    db.init_app(app)
    db.create_all()
    app.run(port=5000, debug=True)

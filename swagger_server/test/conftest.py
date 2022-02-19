import pytest
from app import create_app
from db import db
from models.user import User


@pytest.fixture(scope='module')
def test_client():
    app = create_app(db)
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client


@pytest.fixture(scope='module')
def new_user():
    user = User('TestUser', 'password')
    user.save_to_db()
    return user

import pytest
from app import create_app
from db import db
from models.user import User
from models.category import Category
from models.product import Product
from models.product_category import ProductCategory


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


@pytest.fixture(scope='module')
def init_database(test_client):
    # Create categories
    category_strings = ['home appliances', 'smart watches', 'mobile phones']
    categories = {}
    for category_string in category_strings:
        category = Category(category_string)
        category.save_to_db()
        categories[category_string] = category

    # Create products
    catalog = {
        'refrigerator': {
            'price': 999.99,
            'categories': ['home appliances']
        },
        'galaxy gear': {
            'price': 400.00,
            'categories': ['smart watches']
        },
        'galaxy s22': {
            'price': 1259.00,
            'categories': ['mobile phones']
        }
    }
    for product_name in catalog:
        product = Product(product_name, catalog[product_name]['price'])
        product.save_to_db()

        for category_string in catalog[product_name]['categories']:
            product_category = ProductCategory(
                product.id, categories[category_string].id)
            product_category.save_to_db()

    yield

    db.drop_all()

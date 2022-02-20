from models.user import User
from models.category import Category
from models.product import Product
from models.product_category import ProductCategory


def create_test_user():
    user = User('TestUser', 'password')
    user.save_to_db()
    return user


def create_test_products():
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
        'television': {
            'price': 1309.99,
            'categories': ['home appliances']
        },
        'microwave': {
            'price': 99.90,
            'categories': ['home appliances']
        },
        'galaxy gear': {
            'price': 400.00,
            'categories': ['smart watches']
        },
        'garmin venu 2s': {
            'price': 430.00,
            'categories': ['smart watches']
        },
        'apple watch': {
            'price': 650.00,
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


def create_test_data():
    create_test_user()
    create_test_products()

from flask import request, abort
from flask_restful import Resource
from models.product import Product
from models.product_category import ProductCategory
from marshmellow import Schema, fields


class ProductQuerySchema(Schema):
    category = fields.Str()


class ProductPutSchema(Schema):
    name = fields.Str(required=True)
    price = fields.Decimal(required=True)
    categories = fields.List(fields.Integer(required=True), required=True)


class ProductResource(Resource):
    def get(self):
        schema = ProductQuerySchema()
        errors = schema.validate(request.args)
        if errors:
            abort(400, str(errors))

        args = schema.dump(request)
        products = Product.filter_by_category(args.category)
        return [product.json() for product in products], 200

    def put(self):
        schema = ProductPutSchema()
        errors = schema.validate(request.args)
        if errors:
            abort(400, str(errors))

        args = schema.dump(request)
        product = Product(**args)
        product.save_to_db()

        for category_id in args.categories:
            product_category = ProductCategory(product.id, category_id)
            product_category.save_to_db()

        return product.json(), 201

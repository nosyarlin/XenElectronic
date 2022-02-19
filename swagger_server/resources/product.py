from flask import request, abort
from flask_restful import Resource
from models.product import Product
from marshmellow import Schema, fields


class ProductQuerySchema(Schema):
    category = fields.Str()


class ProductResource(Resource):
    def get(self):
        schema = ProductQuerySchema(request)
        errors = schema.validate(request.args)
        if errors:
            abort(400, str(errors))

        args = schema.dump(request)
        products = Product.filter_by_category(args.category)
        return [product.json() for product in products]

    def put():
        pass

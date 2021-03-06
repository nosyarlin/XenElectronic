from flask import request, abort
from flask_restful import Resource
from models.product import Product
from marshmallow import Schema, fields


class ProductGetSchema(Schema):
    category = fields.Str(required=True)


class ProductResource(Resource):
    def get(self):
        schema = ProductGetSchema()
        errors = schema.validate(request.args)
        if errors:
            abort(400, str(errors))

        args = schema.dump(request.args)
        products = Product.filter_by_category(args['category'])
        return [product.json() for product in products], 200

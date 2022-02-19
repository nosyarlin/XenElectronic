from flask import request, abort
from flask_restful import Resource
from models.product import Product
from marshmallow import Schema, fields


class ProductQuerySchema(Schema):
    category = fields.Str(required=True)


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

        args = schema.dump(request.args)
        products = Product.filter_by_category(args['category'])
        return [product.json() for product in products], 200

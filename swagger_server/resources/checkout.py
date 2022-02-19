from flask import request, abort
from flask_restful import Resource
from models.checkout import Checkout
from models.checkout_product import CheckoutProduct
from marshmallow import Schema, fields


class CheckoutProductPutSchema(Schema):
    productId = fields.Integer(required=True)
    quantity = fields.Integer(required=True)


class CheckoutPutSchema(Schema):
    products = fields.List(
        fields.Nested(CheckoutProductPutSchema),
        required=True
    )


class CheckoutResource(Resource):
    def put(self):
        schema = CheckoutPutSchema()
        errors = schema.validate(request.json)
        if errors:
            abort(400, str(errors))

        # Create Checkout
        userId = request.cookies.get('userID')
        checkout = Checkout(userId)
        checkout.save_to_db()

        # Create CheckoutProducts
        body = schema.dump(request.json)
        products = body['products']
        for product in products:
            checkout_product = CheckoutProduct(
                checkout.id, product['productId'], product['quantity'])
            checkout_product.save_to_db()

        return {'checkoutId': checkout.id}, 201

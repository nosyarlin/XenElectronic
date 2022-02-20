from flask import request, abort
from flask_restful import Resource
from models.user import User
from marshmallow import Schema, fields


class UserCredentialsSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)


class UserPostSchema(Schema):
    credentials = fields.Nested(UserCredentialsSchema)


class UserResource(Resource):
    def post(self):
        schema = UserPostSchema()
        errors = schema.validate(request.json)
        if errors:
            abort(400, str(errors))

        body = schema.dump(request.json)
        user = User.find_by_username(body['credentials']['username'])
        if user is None or user.password != body['credentials']['password']:
            abort(401, 'Incorrect username or password')

        return {'success': True}, 200, {'Set-Cookie': 'userId={}'.format(user.id)}

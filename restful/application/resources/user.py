from flask_restful import Resource
from application.schemas.user import UserSchema
from application.controllers.user import UserController
from webargs.flaskparser import use_args, use_kwargs

class User(Resource):
    def get(self, id):
        user = UserController().getUserByID(id)
        if user:
            return UserSchema().dump(user).data
        return 'User not found', 404

    @use_args(UserSchema())
    def put(self, args):
        UserController().updateUser()
        return UserSchema().dump(args).data, 200

    def delete(self, id):
        UserController().deleteUser(id)
        return 'User removed', 200

class Users(Resource):

    @use_args(UserSchema(many = True))
    def post(self, args):
        UserController().addUser(args)
        return UserSchema(many = True).dump(args).data, 201

    def get(self):
        users = UserController().getUsers()
        return  UserSchema(many = True).dump(users).data, 201
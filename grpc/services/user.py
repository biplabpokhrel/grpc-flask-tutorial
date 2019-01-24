import grpc
import user_pb2_grpc as user_service
import user_pb2 as user_messages
import logging
from application.app import app
from application.controllers.user import UserController
import time
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp

class UserService(user_service.UserServicer):

    def GetUser(self, request, context):
        if request.id:
            with app.app_context():
                user = UserController().getUserByID(id = request.id)
                logging.debug(user)
                if user:
                    return user_messages.UserResponse( \
                               id = user.id, \
                               name = user.name, \
                               birth = self.convertIntoTimestamp(user.birth), \
                               gender = user.gender.upper())
                msg = 'User ID not found'
                context.set_details(msg)
                context.set_code(grpc.StatusCode.NOT_FOUND)
                return user_messages.UserResponse()
        msg = 'Must pass ID'
        context.set_details(msg)
        context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
        return user_messages.UserResponse()

    def GetUsers(self, request, context):
        with app.app_context():
            if request and request.name:
                for name in request.name:
                    for user in UserController().getUsersByName(name = name):
                        yield user_messages.UserResponse( \
                               id = user.id, \
                               name = user.name, \
                               birth = self.convertIntoTimestamp(user.birth), \
                               gender = user.gender.upper())
            else:
                for user in UserController().getUsers():
                    yield user_messages.UserResponse( \
                               id = user.id, \
                               name = user.name, \
                               birth = self.convertIntoTimestamp(user.birth), \
                               gender = user.gender.upper())

    def convertIntoTimestamp(self, old_date):
        ts = Timestamp()
        new_date = datetime.combine(old_date, datetime.min.time())
        ts.FromDatetime(new_date)
        return ts


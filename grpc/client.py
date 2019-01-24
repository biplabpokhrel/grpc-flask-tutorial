import grpc
import messages.user_pb2_grpc as user_service
import messages.user_pb2 as user_messages

# FYI : This is junst an example how to use the existing GRPC services

def get_user(id):
    channel = grpc.insecure_channel("127.0.0.1:50051")
    client = user_service.UserStub(channel)
    response = client.GetUser(user_messages.UserRequest(id=id))
    if response:
        print( "ID: {}".format(response.id))
        print( "Name: {}".format(response.name))
        print( "Gender: {}".format(response.gender))
        print( "DOB: {}".format(response.birth.ToDatetime()))

def get_users(name=[]):
    channel = grpc.insecure_channel("127.0.0.1:50051")
    client = user_service.UserStub(channel)
    responses = client.GetUsers(user_messages.UsersRequest(name=name))
    for response in responses:
        print( "ID: {}".format(response.id))
        print( "Name: {}".format(response.name))
        print( "Gender: {}".format(response.gender))
        print( "DOB: {}".format(response.birth.ToDatetime()))

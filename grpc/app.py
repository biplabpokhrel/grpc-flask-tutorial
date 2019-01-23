from  concurrent import futures
import time
import grpc
import messages.user_pb2_grpc as user_service
from services.user import UserService
import logging
_ONE_DAY_IN_SECONDS = 60 * 60 * 24

def grpc_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Register user service
    user_serve = UserService()
    user_service.add_UserServicer_to_server(user_serve, server)

    logging.info('GRPC running')
    # This is just for testing onyl ( Not recommended in production )
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        logging.debug('GRPC stop')
        server.stop(0)
if __name__ == '__main__':
    grpc_server()

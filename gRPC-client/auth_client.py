import grpc  # type: ignore

from logger import logging
from protos import auth_pb2, auth_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = auth_pb2_grpc.AuthServiceStub(channel)
        username = input("Введите логин: ")
        password = input("Введите пароль: ")
        response = stub.login(
            auth_pb2.LoginRequest(username=username, password=password)
        )
        logging.info(response.message)


if __name__ == "__main__":
    run()

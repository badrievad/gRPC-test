from protos import auth_pb2, auth_pb2_grpc

# Используем словарь для хранения пользователей (тест)
users = {"user1": "password1", "user2": "password2"}


class AuthService(auth_pb2_grpc.AuthServiceServicer):
    def login(self, request, context):
        username = request.username
        password = request.password

        # Проверяем учетные данные пользователя
        if username in users and users[username] == password:
            return auth_pb2.LoginResponse(success=True, message="Вы вошли")
        else:
            return auth_pb2.LoginResponse(
                success=False, message="Неправильный логин/пароль"
            )

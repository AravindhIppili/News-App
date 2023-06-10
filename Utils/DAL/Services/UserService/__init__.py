from ...Models.models import User, Token
from ...Models.shemas import UserCreateSchema, UserLoginSchema
import bcrypt
from Exceptions import UserExists, UnAuthorized
from Responses import Responses
from typing import Any


class UserService:
    def initConnection(self):
        self.user_model.initConnection()
        self.token_model.initConnection()

    def __init__(self, *args, **kwargs):
        self.user_model = kwargs.get("user_model", User())
        self.token_model = kwargs.get("token_model", Token())
        super().__init__(*args, **kwargs)

    def hashPassword(self, password: str) -> bytes:
        encoded_string = password.encode("utf-8")
        salt = bcrypt.gensalt(rounds=12)
        return bcrypt.hashpw(encoded_string, salt)

    def verifyPassword(self, hash: str, string: str) -> bool:
        encoded_string = string.encode("utf-8")
        hash = hash.encode("utf-8")
        return bcrypt.checkpw(encoded_string, hash)

    def get_user(self, email: str, username: str) -> Any:
        user = self.user_model.get(email=email)
        if user:
            return user
        user = self.user_model.get(username=username)

        if user:
            return user
        return False

    def create_user(self, user_info: UserCreateSchema) -> User:
        if self.get_user(email=user_info.email, username=user_info.username):
            raise UserExists(Responses.getResponse("user_exists"))

        user_info_dict = user_info.dict()

        password = user_info_dict.pop("password")

        if password:
            user_info_dict["password"] = self.hashPassword(password)
        user = self.user_model.create(**user_info_dict)
        return user

    def login_user(self, user_info: UserLoginSchema) -> User:
        user = self.get_user(username=user_info.username, email=user_info.username)
        if not user or not self.verifyPassword(user.password, user_info.password):
            raise UnAuthorized(Responses.getResponse("user_not_found"))
        return {
            "access_token": "a",
        }

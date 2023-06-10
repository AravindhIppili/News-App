from pydantic import BaseModel, EmailStr
from .models import User


class UserCreateSchema(BaseModel):
    email: EmailStr
    username: str
    password: str
    userType: str = User.USER


class UserLoginSchema(BaseModel):
    username: str
    password: str

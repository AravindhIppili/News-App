from .Router import v1_router as router
from Utils.DAL.Models.shemas import UserCreateSchema, UserLoginSchema
from Utils.DAL.Models.models import User
from Utils.DAL.Services.UserService import UserService
from ConfigManager import Config
from fastapi.responses import JSONResponse
from Responses import Responses


@router.post("/user/create")
async def create_user(user_info: UserCreateSchema):
    if user_info.userType != User.USER:
        pass

    user_service: UserService = Config.get("user_service")
    user = user_service.create_user(user_info)
    return JSONResponse(
        status_code=201, content={"details": "User Created!", "username": user.username}
    )


@router.post("/user/login")
async def create_user(user_info: UserLoginSchema):
    user_service: UserService = Config.get("user_service")
    details = user_service.login_user(user_info)
    return details

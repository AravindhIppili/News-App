from fastapi import Request
from typing import Any
from .Base import BaseMiddleware
from Exceptions import UnAuthorized
from Responses import Responses
from ConfigManager import Config


class isAuthenticated(BaseMiddleware):
    def __init__(self, app, paths) -> None:
        super().__init__(app, paths)

    async def dispatch(self, request: Request, call_next) -> Any:
        if not request.headers.get("Authorization") and request.url.path in self.paths:
            raise UnAuthorized(Responses.getResponse("un_authorized"))
        token = request.headers.get("Authorization")
        if token != Config.get("APP_KEY"):
            raise UnAuthorized(Responses.getResponse("not_valid_token"))
        return await call_next(request)

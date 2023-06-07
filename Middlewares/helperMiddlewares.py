from fastapi import Request
from Exceptions import ValidationError
from Responses import Responses
from typing import Any
from .Base import BaseMiddleware


class BodyRequiredMiddleware(BaseMiddleware):
    def __init__(self, app, paths) -> None:
        super().__init__(app, paths)

    async def dispatch(self, request: Request, call_next) -> Any:
        await self.set_body(request, await request.body())
        body = await self.get_body(request)

        if not body and request.method == "POST" and request.url.path in self.paths:
            raise ValidationError(Responses.getResponse("body_required"))
        return await call_next(request)

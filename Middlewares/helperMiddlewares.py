from fastapi import Request
from Exceptions import ValidationError
from Responses import Responses
from starlette.middleware.base import BaseHTTPMiddleware
from typing import Any


class BaseMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, paths) -> None:
        super().__init__(app)
        self.paths = paths

    async def set_body(self, request: Request, body: bytes, json_body: Any) -> None:
        async def receive():
            return {"type": "http.request", "body": body, "json": json_body}

        request._receive = receive

    async def get_body(self, request: Request) -> bytes:
        body = await request.body()
        await self.set_body(request, body, await request.json() if body else None)
        return body


class BodyRequiredMiddleware(BaseMiddleware):
    def __init__(self, app, paths) -> None:
        super().__init__(app, paths)

    async def dispatch(self, request: Request, call_next) -> Any:
        body = await request.body()
        await self.set_body(request, body, await request.json() if body else None)
        body = await self.get_body(request)

        if not body and request.method == "POST" and request.url.path in self.paths:
            raise ValidationError(Responses.getResponse("body_required"))
        return await call_next(request)

from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from typing import Any


class BaseMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, paths) -> None:
        super().__init__(app)
        self.paths = paths

    async def set_body(
        self,
        request: Request,
        body: bytes,
    ) -> None:
        async def receive():
            return {
                "type": "http.request",
                "body": body,
                "json": await request.json() if body else None,
            }

        request._receive = receive

    async def get_body(self, request: Request) -> bytes:
        body = await request.body()
        await self.set_body(request, body)
        return body

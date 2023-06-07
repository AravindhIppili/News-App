from .helperMiddlewares import *
from .permissionMiddlewares import *

from fastapi import FastAPI


def add_middlewares(app: FastAPI):
    app.add_middleware(BodyRequiredMiddleware, paths=["/api/v1/news/getnews"])
    app.add_middleware(isAuthenticated, paths=["/api/v1/news/getnews"])

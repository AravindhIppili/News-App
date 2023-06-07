from fastapi import FastAPI
from Routes.v1.Router import v1_router
from initConfig import initConfig
from Exceptions.Handler import exceptionHandler
from Middlewares import BodyRequiredMiddleware


app = FastAPI()

app.include_router(router=v1_router, prefix="/api/v1/news")
app.add_middleware(BodyRequiredMiddleware, paths=["/api/v1/news/getnews"])

initConfig("dev")


@app.exception_handler(Exception)
async def handleExceptions(request, exception):
    return exceptionHandler(exception)


@app.get("/")
async def root():
    return {"message": "Healthy"}

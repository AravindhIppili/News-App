from fastapi import FastAPI
from Routes.v1.Router import v1_router
from initConfig import initConfig
from Exceptions.Handler import exceptionHandler
from Middlewares import add_middlewares

app = FastAPI()

app.include_router(router=v1_router, prefix="/api/v1")
add_middlewares(app)

initConfig("dev")


@app.exception_handler(Exception)
async def handleExceptions(request, exception):
    return exceptionHandler(exception)


@app.get("/")
async def root():
    return {"message": "Healthy"}

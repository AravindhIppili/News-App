from fastapi import FastAPI
from Routes.v1.Router import v1_router
from initConfig import initConfig

app = FastAPI()


app.include_router(router=v1_router, prefix="/api/v1/news")


initConfig("dev")


@app.get("/")
async def root():
    return {"message": "Health"}

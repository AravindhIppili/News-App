from .Router import v1_router as router
import json


@router.post("/getnews")
async def get_news():
    return "abc"

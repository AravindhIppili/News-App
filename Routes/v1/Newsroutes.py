from .Router import v1_router as router
import json
from Services.NewsApi.fetcher import NewsApiFetcher
from ConfigManager import Config


@router.post("/getnews")
async def get_news(and_k: list[str], not_k: list[str]):
    print(and_k, not_k)
    # news_api_fetcher: NewsApiFetcher = NewsApiFetcher(Config.get("NEWS_API_KEY"))
    # articles = news_api_fetcher(filters)
    return "articles"

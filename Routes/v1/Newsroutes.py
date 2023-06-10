from .Router import v1_router as router
import json
from Utils.Services.NewsApi.fetcher import NewsApiFetcher
from ConfigManager import Config


@router.post("/news/getnews")
async def get_news(and_k: list[str], not_k: list[str]) -> list[dict]:
    news_api_fetcher: NewsApiFetcher = NewsApiFetcher(Config.get("NEWS_API_KEY"))
    articles = news_api_fetcher(and_k=and_k, not_k=not_k)
    return [article.dict() for article in articles]

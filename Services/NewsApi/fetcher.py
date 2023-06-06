from typing import Any
from eventregistry import *


class NewsApiFetcher:
    def __init__(self, NEWS_API_KEY: str):
        self.NEWS_API_KEY = NEWS_API_KEY
        self.news_api_client = EventRegistry(
            apiKey=self.NEWS_API_KEY, allowUseOfArchive=False
        )

    def __call__(self, filters: dict) -> Any:
        query = QueryArticlesIter(**filters)
        articles = []
        for article in query.execQuery(
            self.news_api_client, sortBy="date", sortByAsc=False, maxItems=10
        ):
            articles.append(article)
        return articles

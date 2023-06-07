from typing import Any
from eventregistry import *
from .article import Article
from ConfigManager import Config


class NewsApiFetcher:
    def __init__(self, NEWS_API_KEY: str):
        self.NEWS_API_KEY = NEWS_API_KEY
        self.news_api_client = EventRegistry(
            apiKey=self.NEWS_API_KEY, allowUseOfArchive=False
        )

    def parse_filters(self, filters: dict):
        return {
            "keywords": QueryItems.AND(filters.get("and_k")),
            "lang": filters.get("lang"),
            "ignoreKeywords": QueryItems.OR(filters.get("not_k")),
            "startSourceRankPercentile": 0,
            "endSourceRankPercentile": 30,
            "dataType": filters.get("dataType"),
        }

    def __call__(self, **filters: dict) -> Any:
        parsed_filters = self.parse_filters(
            {**filters, "lang": ["eng"], "dataType": ["news", "blog"]}
        )
        query = QueryArticlesIter(**parsed_filters)
        articles = []
        for article in query.execQuery(
            self.news_api_client,
            sortBy="date",
            sortByAsc=False,
            maxItems=Config.get("NEWSAPI_MAX_ARTICLES"),
        ):
            articles.append(Article(**article))
        return articles

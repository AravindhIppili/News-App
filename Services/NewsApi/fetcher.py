from typing import Any
from eventregistry import *


class NewsApiFetcher:
    def __init__(self, NEWS_API_KEY: str):
        self.NEWS_API_KEY = NEWS_API_KEY
        self.news_api_client = EventRegistry(
            apiKey=self.NEWS_API_KEY, allowUseOfArchive=False
        )
        print(self.news_api_client)

    def parse_filters(filters: dict):
        return {
            "keywords": QueryItems.AND(filters.get("and_k")),
            "lang": filters.get("lang"),
            "ignoreKeywords": QueryItems.OR(filters.get("not_k")),
            "startSourceRankPercentile": 0,
            "endSourceRankPercentile": 30,
            "dataType": filters.get("dataType"),
        }

    def __call__(self, filters: dict) -> Any:
        parsed_filters = self.parse_filters(
            filters, lang=["eng"], dataType=["news", "blog"]
        )
        print(parsed_filters)
        # query = QueryArticlesIter(**parsed_filters)
        articles = []
        # for article in query.execQuery(
        #     self.news_api_client, sortBy="date", sortByAsc=False, maxItems=10
        # ):
        #     articles.append(article)
        return articles

from dataclasses import dataclass
from datetime import datetime
from typing import List, Any


@dataclass
class Article:
    uri: int
    url: str
    title: str
    body: str
    date: datetime
    time: datetime
    date_time: datetime
    date_time_pub: datetime
    lang: str
    is_duplicate: bool
    data_type: str
    image: str
    source: dict
    categories: List[Any]
    concepts: List[Any]
    links: List[str]
    videos: List[dict]

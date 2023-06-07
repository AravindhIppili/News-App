from datetime import datetime
from typing import List, Any, Dict, Optional
from pydantic import BaseModel


class Article(BaseModel):
    uri: Optional[str]
    url: str
    title: str
    body: str
    date: str
    time: str
    date_time: Optional[str]
    date_time_pub: Optional[str]
    lang: Optional[str]
    is_duplicate: Optional[bool]
    data_type: Optional[str]
    image: Optional[str]
    source: Optional[Dict[str, Any]]
    categories: Optional[List[Any]]
    concepts: Optional[List[Any]]
    links: Optional[List[str]]
    videos: Optional[List[Dict[str, Any]]]

from dataclasses import dataclass
from datetime import datetime
from typing import List, Any


@dataclass
class ExtractedDate:
    amb: bool
    date: datetime
    date_end: datetime
    detected_date: str
    imp: bool
    pos_in_text: int
    text_snippet: str


@dataclass
class Shares:
    facebook: int
    google_plus: int
    pinterest: int
    linked_in: int


@dataclass
class Source:
    pass


@dataclass
class Video:
    uri: str
    label: str


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
    sentiment: float
    event_uri: str
    relevance: int
    story_uri: str
    image: str
    source: Source
    categories: List[Any]
    concepts: List[Any]
    links: List[str]
    videos: List[Video]
    shares: Shares
    duplicate_list: List[Any]
    extracted_dates: List[ExtractedDate]
    location: None
    original_article: None
    sim: float
    wgt: int

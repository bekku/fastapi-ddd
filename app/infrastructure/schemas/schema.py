from datetime import datetime
from typing import List
from dataclasses import dataclass

@dataclass
class ArticleResponse:
    id: int
    title: str
    created_at: datetime
    url: str
    categories: List[str]
    content: str
    total_views: int
    summary_content: str

@dataclass
class ArticleCreate:
    title: str
    url: str
    categories: List[str]
    content: str
    summary_content: str
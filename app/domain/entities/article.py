from datetime import datetime
from typing import List
from dataclasses import dataclass

@dataclass
class Article:
    id: int
    title: str
    created_at: datetime
    url: str
    categories: List[str]
    content: str
    total_views: int
    summary_content: str
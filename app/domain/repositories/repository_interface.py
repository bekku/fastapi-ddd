from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.article import Article

class ArticleDbRepository(ABC):
    @abstractmethod
    def save(self, article: Article) -> Article:
        pass

    @abstractmethod
    def get_all(self) -> list[Article]:
        pass

    @abstractmethod
    def get_by_id(self, article_id: int) -> Article:
        pass


class ArticleApiRepository(ABC):
    # 外部API経由で作成
    @abstractmethod
    def create_via_api(self, article: Article) -> list[Article]:
        pass
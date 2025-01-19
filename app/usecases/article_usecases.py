from typing import List
from app.domain.entities.article import Article
from app.domain.repositories.repository_interface import ArticleDbRepository

class ArticleUsecase:
    def __init__(self, db_repository: ArticleDbRepository):
        self.db_repository = db_repository  # データベース用

    def create_article(self, article: Article) -> Article:
        created_article: Article = self.db_repository.save(article)
        return created_article

    def list_articles(self) -> List[Article]:
        list_articles: list[Article] = self.db_repository.get_all()
        return list_articles

    def get_article(self, article_id: int) -> Article:
        get_article: Article = self.db_repository.get_by_id(article_id)
        return get_article


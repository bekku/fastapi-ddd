from typing import List, Optional
from sqlalchemy.orm import Session
from app.domain.entities.article import Article
from app.domain.repositories.repository_interface import ArticleDbRepository
from app.infrastructure.sqlite.models import ArticleDB
from datetime import datetime

class SQLAlchemyArticleDbRepository(ArticleDbRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, article: Article) -> Article:
        # 保存する新規オブジェクトを作成
        article_db = ArticleDB(
            title=article.title,
            created_at=datetime.now(),
            url=article.url,
            categories=article.categories,
            content=article.content,
            total_views=0,
            summary_content=article.summary_content,
        )
        self.session.add(article_db)
        self.session.commit()
        return Article(
                id=article_db.id,
                title=article_db.title,
                created_at=article_db.created_at,
                url=article_db.url,
                categories=article_db.categories,
                content=article_db.content,
                total_views=article_db.total_views,
                summary_content=article.summary_content,
            )

    def get_all(self) -> List[Article]:
        return [
            Article(
                id=article.id,
                title=article.title,
                created_at=article.created_at,
                url=article.url,
                categories=article.categories,
                content=article.content,
                total_views=article.total_views,
                summary_content=article.summary_content,
            )
            for article in self.session.query(ArticleDB).all()
        ]

    def get_by_id(self, article_id: int) -> Optional[Article]:
        article_db = self.session.query(ArticleDB).filter(ArticleDB.id == article_id).first()
        if article_db:
            return Article(
                id=article_db.id,
                title=article_db.title,
                created_at=article_db.created_at,
                url=article_db.url,
                categories=article_db.categories,
                content=article_db.content,
                total_views=article_db.total_views,
                summary_content=article.summary_content,
            )
        return None



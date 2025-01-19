from app.infrastructure.sqlite.database import Base
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.dialects.sqlite import JSON
from datetime import datetime

class ArticleDB(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    url = Column(String, nullable=False)
    categories = Column(JSON, default=[])
    content = Column(Text, nullable=False)
    total_views = Column(Integer, default=0)
    summary_content = Column(String, nullable=False, default="")

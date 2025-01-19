from fastapi import APIRouter, Depends
from typing import List
from dataclasses import asdict
from app.infrastructure.sqlite.database import SessionLocal
from app.infrastructure.sqlite.repositories import SQLAlchemyArticleDbRepository
from app.usecases.article_usecases import ArticleUsecase
from app.infrastructure.schemas.schema import ArticleResponse, ArticleCreate

router = APIRouter()

def get_article_usecase():
    db = SessionLocal()
    # 依存注入
    db_repository = SQLAlchemyArticleDbRepository(db)
    return ArticleUsecase(db_repository=db_repository)

@router.get("/articles", response_model=List[ArticleResponse])
def list_articles(usecase: ArticleUsecase = Depends(get_article_usecase)):
    list_articles = usecase.list_articles()
    return [ArticleResponse(**asdict(article)) for article in list_articles]

@router.get("/articles/{article_id}", response_model=ArticleResponse)
def get_article(article_id: int, usecase: ArticleUsecase = Depends(get_article_usecase)):
    get_article = usecase.get_article(article_id)
    print(asdict(get_article))
    return ArticleResponse(**asdict(get_article))

@router.post("/post_articles", response_model=ArticleResponse)
def create_article(article: ArticleCreate, usecase: ArticleUsecase = Depends(get_article_usecase)):
    created_article =usecase.create_article(article)
    return ArticleResponse(**asdict(created_article))

# @router.get("/auto_create_articles/")
# def auto_create_article_via_api(usecase: AutoCreateArticleUsecase = Depends(get_article_usecase)):
#     usecase.create_article_via_api(Article(**asdict(article)))

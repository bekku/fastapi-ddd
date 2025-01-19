from fastapi import FastAPI
from app.infrastructure.api.routes import router as article_router
from app.infrastructure.sqlite.database import Base, engine

# データベーステーブルの作成
Base.metadata.create_all(bind=engine)

# FastAPI アプリケーションの初期化
app = FastAPI(
    title="Article Management API",
    description="A simple API to manage articles with Clean Architecture.",
    version="1.0.0"
)

# ルータの登録
app.include_router(article_router, prefix="/api", tags=["Articles"])

# アプリ起動時イベント
@app.on_event("startup")
async def startup_event():
    print("Application has started!")

# アプリ終了時イベント
@app.on_event("shutdown")
async def shutdown_event():
    print("Application is shutting down!")

from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./app/infrastructure/sqlite/db/articles.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# このセッションを基にDBを操作する
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# model作成用の引き継ぎ元クラス
Base = declarative_base()
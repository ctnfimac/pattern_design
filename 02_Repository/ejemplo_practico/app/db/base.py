from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_POSTGRES_URL = 'postgresql://christian:123456@localhost:3009/repositorydb'

engine = create_engine(
    SQLALCHEMY_DATABASE_POSTGRES_URL,
    echo=True,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
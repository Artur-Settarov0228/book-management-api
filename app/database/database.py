from sqlalchemy import create_engine, URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2

from app.core import config

DATABASE_URL = URL.create(
    drivername='postgresql+psycopg2',
    host= config.DB_HOST,
    port=config.DB_PORT,
    username=config.DB_PASS,
    database=config.DB_NAME
)

engine = create_engine(url=DATABASE_URL)
Base = declarative_base()


SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
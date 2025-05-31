from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:xxxxxx@localhost:5432/postgres?connect_timeout=10&sslmode=prefer" #trocar a senha

engine = create_engine("postgresql://postgres:xxxxxx@localhost:5432/postgres?connect_timeout=10&sslmode=prefer")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
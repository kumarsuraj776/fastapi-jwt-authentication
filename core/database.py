from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import Generator
from core.config import get_settings

# Initializing the configuration
settings = get_settings()

# Creating the database engine
engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False}  # Necessary for SQLite
)
# Creating the session maker
SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base=declarative_base()

# Creating the database connection
def get_db()->Generator:
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

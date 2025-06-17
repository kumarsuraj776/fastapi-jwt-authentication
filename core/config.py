import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

env_path=Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):
    # Path to your SQLite database file
    DB_PATH: str = os.getenv("SQLITE_DB_PATH", "sqlite.db")
    DATABASE_URL: str = f"sqlite:///{DB_PATH}"
    
    # JWT 
    JWT_SECRET:str = os.getenv("JWT_SECRET", "13245shdgahslajwdklajdhasjdhjldkewlkdj")
    JWT_ALGORITHM:str = os.getenv("JWT_ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES:int = os.getenv("JWT_TOKEN_EXPIRE_MINUTES", 30)
    REFRESH_TOKEN_EXPIRE_MINUTES:int = os.getenv("JWT_REFRESH_TOKEN_EXPIRE_MINUTES", 3600*24*7)
    

def get_settings()->Settings:
    return Settings()
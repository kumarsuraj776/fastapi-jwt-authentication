from sqlalchemy import Column, String, Boolean, DateTime, Integer
from sqlalchemy.sql import func
from core.database import Base

class User(Base):
    __tablename__="users"
    
    id=Column(Integer, primary_key=True, index=True)
    first_name=Column(String(30), nullable=False)
    last_name=Column(String(30), nullable=False)
    email=Column(String(50), nullable=False, unique=True)
    password=Column(String(100), nullable=False)
    is_active=Column(Boolean, default=True)
    is_verified=Column(Boolean, default=False)
    verified_at=Column(DateTime(timezone=True), nullable=True, default=None)
    created_at=Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at=Column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())
    
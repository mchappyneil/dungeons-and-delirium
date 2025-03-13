from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String

import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# Create async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Session
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Base model
Base = declarative_base()

# Character model
class Character(Base):
    __tablename__ = "characters"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    class_type = Column(String, nullable=False)
    level = Column(Integer, default=1)
    hit_points = Column(Integer, default=10)
    stats = Column(String) # Store stats as JSON string
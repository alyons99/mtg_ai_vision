from sqlmodel import SQLModel, Field, create_engine, Session
from datetime import datetime
from typing import Optional
import os
from dotenv import load_dotenv

class CardSearch(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    card_name: str
    set_name: Optional[str] = None
    tcg_price: Optional[float] = None
    ebay_price: Optional[float] = None
    file_name: str
    created: datetime = Field(default_factory=datetime.utcnow)

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True)
    password: str
    created: datetime = Field(default_factory=datetime.utcnow)

class Favorite(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    card_id: int = Field(foreign_key="cardsearch.id")
    created: datetime = Field(default_factory=datetime.utcnow)

load_dotenv()
# Get database configuration from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT", "5432")  # Default PostgreSQL port

# Create the database URL
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
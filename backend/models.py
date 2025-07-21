from sqlmodel import SQLModel, Field, create_engine, Session
from datetime import datetime
from typing import Optional
import os
from dotenv import load_dotenv

class CardSearch():
    pass

class User():
    pass

class Favorite():
    pass

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
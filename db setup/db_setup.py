import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models_db import Base

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "db", "users.db")
engine = create_engine(f"sqlite:///{DB_PATH}")
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)

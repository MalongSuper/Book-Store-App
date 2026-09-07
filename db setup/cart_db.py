import os

from sqlalchemy import Column, String, Float, Integer, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "db", "cart.db")

class CartItem(Base):
    __tablename__ = "cart"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_email = Column(String)
    book_title = Column(String)
    price = Column(Float)
    quantity = Column(Integer)

engine = create_engine(f"sqlite:///{DB_PATH}")
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)


def delete_cart_by_email(email):
    db = SessionLocal()
    db.query(CartItem).filter(CartItem.user_email == email).delete()
    db.commit()
    db.close()

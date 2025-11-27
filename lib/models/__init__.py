from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///book_collection.db')
Session = sessionmaker(bind=engine)
session = Session()

from .book import Book
from .author import Author
from .genre import Genre
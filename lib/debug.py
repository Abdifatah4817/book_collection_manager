#!/usr/bin/env python3

# FIXED IMPORTS - Remove 'lib.' prefix
from models import session, Author, Genre, Book
from database.setup import create_tables
from helpers import seed_database

def debug():
    """Debug function to test the models and relationships"""
    create_tables()
    
    # Create authors
    author1 = Author.create(session, "J.K. Rowling", "British")
    author2 = Author.create(session, "George Orwell", "British")
    
    # Create genres
    genre1 = Genre.create(session, "Fantasy", "Magical and supernatural elements")
    genre2 = Genre.create(session, "Science Fiction", "Futuristic and scientific themes")
    
    # Create books
    book1 = Book.create(session, "Harry Potter and the Philosopher's Stone", 
                        "978-0439708180", 1997, author1.id, genre1.id, 4.8, 320)
    
    book2 = Book.create(session, "1984", "978-0451524935", 1949, author2.id, genre2.id, 4.7, 328)
    
    # Test relationships
    print(f"\nAuthor '{author1.name}' has {author1.book_count} books:")
    for book in author1.books:
        print(f"  - {book.title}")
    
    print(f"\nGenre '{genre1.name}' has {genre1.book_count} books:")
    for book in genre1.books:
        print(f"  - {book.title}")
    
    print(f"\nBook '{book1.title}' reading time: {book1.reading_time}")
    print(f"Book '{book2.title}' reading time: {book2.reading_time}")
    
    # Test queries
    print(f"\nAll books: {len(Book.get_all(session))}")
    print(f"All authors: {len(Author.get_all(session))}")
    print(f"All genres: {len(Genre.get_all(session))}")

if __name__ == "__main__":
    debug()

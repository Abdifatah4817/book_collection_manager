from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from . import Base  # FIXED: Use relative import

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    isbn = Column(String, unique=True)
    publication_year = Column(Integer)
    rating = Column(Float)
    pages = Column(Integer)
    
    # Foreign keys
    author_id = Column(Integer, ForeignKey('authors.id'))
    genre_id = Column(Integer, ForeignKey('genres.id'))
    
    # Relationships
    author = relationship("Author", back_populates="books")
    genre = relationship("Genre", back_populates="books")
    
    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', author='{self.author.name if self.author else None}')>"
    
    @classmethod
    def create_book(cls, title, isbn, publication_year, author_id, genre_id, rating=0.0, pages=0):
        """Create a new book"""
        from . import session  # FIXED: Import session locally
        book = cls(
            title=title,
            isbn=isbn,
            publication_year=publication_year,
            author_id=author_id,
            genre_id=genre_id,
            rating=rating,
            pages=pages
        )
        session.add(book)
        session.commit()
        return book
    
    @classmethod
    def get_all_books(cls):
        """Get all books"""
        from . import session  # FIXED: Import session locally
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, book_id):
        """Find book by ID"""
        from . import session
        return session.query(cls).filter(cls.id == book_id).first()
    
    @classmethod
    def find_by_title(cls, title):
        """Find book by title"""
        from . import session
        return session.query(cls).filter(cls.title.ilike(f"%{title}%")).all()
    
    @classmethod
    def find_by_author(cls, author_id):
        """Find books by author"""
        from . import session
        return session.query(cls).filter(cls.author_id == author_id).all()
    
    @classmethod
    def find_by_genre(cls, genre_id):
        """Find books by genre"""
        from . import session
        return session.query(cls).filter(cls.genre_id == genre_id).all()
    
    @classmethod
    def delete_book(cls, book_id):
        """Delete book by ID"""
        from . import session
        book = cls.find_by_id(book_id)
        if book:
            session.delete(book)
            session.commit()
            return True
        return False
    
    @classmethod
    def update_rating(cls, book_id, rating):
        """Update book rating"""
        from . import session
        book = cls.find_by_id(book_id)
        if book:
            book.rating = rating
            session.commit()
            return True
        return False
    
    @property
    def reading_time(self):
        """Estimate reading time (assuming 200 words per minute, 250 words per page)"""
        if self.pages:
            words = self.pages * 250
            minutes = words / 200
            hours = minutes / 60
            return f"{hours:.1f} hours"
        return "Unknown"
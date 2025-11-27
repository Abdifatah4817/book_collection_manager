from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import relationship
from . import Base  # FIXED: Use relative import

class Author(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    nationality = Column(String)
    
    # One-to-many relationship with books
    books = relationship("Book", back_populates="author")
    
    def __repr__(self):
        return f"<Author(id={self.id}, name='{self.name}', nationality='{self.nationality}')>"
    
    @classmethod
    def create_author(cls, name, nationality):
        """Create a new author"""
        from . import session  # FIXED: Import session locally
        author = cls(name=name, nationality=nationality)
        session.add(author)
        session.commit()
        return author
    
    @classmethod
    def get_all_authors(cls):
        """Get all authors"""
        from . import session
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, author_id):
        """Find author by ID"""
        from . import session
        return session.query(cls).filter(cls.id == author_id).first()
    
    @classmethod
    def find_by_name(cls, name):
        """Find author by name"""
        from . import session
        return session.query(cls).filter(cls.name.ilike(f"%{name}%")).all()
    
    @classmethod
    def delete_author(cls, author_id):
        """Delete author by ID"""
        from . import session
        author = cls.find_by_id(author_id)
        if author:
            session.delete(author)
            session.commit()
            return True
        return False
    
    @property
    def book_count(self):
        """Return number of books by this author"""
        return len(self.books)
    
    def get_books(self):
        """Get all books by this author"""
        return self.books
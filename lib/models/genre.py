from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base  # FIXED: Use relative import

class Genre(Base):
    __tablename__ = 'genres'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    description = Column(String)
    
    # Many-to-many relationship with books (through book_genre association)
    books = relationship("Book", back_populates="genre")
    
    def __repr__(self):
        return f"<Genre(id={self.id}, name='{self.name}', description='{self.description}')>"
    
    @classmethod
    def create_genre(cls, name, description=""):
        """Create a new genre"""
        from . import session  # FIXED: Import session locally
        genre = cls(name=name, description=description)
        session.add(genre)
        session.commit()
        return genre
    
    @classmethod
    def get_all_genres(cls):
        """Get all genres"""
        from . import session
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, genre_id):
        """Find genre by ID"""
        from . import session
        return session.query(cls).filter(cls.id == genre_id).first()
    
    @classmethod
    def find_by_name(cls, name):
        """Find genre by name"""
        from . import session
        return session.query(cls).filter(cls.name.ilike(f"%{name}%")).all()
    
    @classmethod
    def delete_genre(cls, genre_id):
        """Delete genre by ID"""
        from . import session
        genre = cls.find_by_id(genre_id)
        if genre:
            session.delete(genre)
            session.commit()
            return True
        return False
    
    @property
    def book_count(self):
        """Return number of books in this genre"""
        return len(self.books)
from models import Base, engine  # FIXED: Direct import

def create_tables():
    """Create all tables in the database"""
    Base.metadata.create_all(engine)
    print("Database tables created successfully!")

def reset_database():
    """Drop and recreate all tables"""
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("Database reset successfully!")
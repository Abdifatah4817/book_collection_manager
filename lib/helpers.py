from models import Author, Genre, Book, session
from faker import Faker

fake = Faker()

def exit_program():
    """Exit the program"""
    print("Thank you for using Book Collection Manager!")
    exit()

def seed_database():
    """Seed the database with sample data (only if empty)"""
    # Check if database already has data
    existing_books = Book.get_all_books()
    if existing_books:
        print("Database already has data. Skipping seed.")
        return
    
    print("Seeding database with sample data...")
    
    # Create genres
    genres_data = [
        ("Fiction", "Imaginative literary works"),
        ("Science Fiction", "Futuristic and scientific themes"),
        ("Mystery", "Crime and detective stories"),
        ("Romance", "Love and relationship stories"),
        ("Non-Fiction", "Factual and informative works"),
        ("Fantasy", "Magical and supernatural elements")
    ]
    
    genres = []
    for name, description in genres_data:
        genre = Genre.create_genre(name, description)
        genres.append(genre)
    
    # Create authors
    authors_data = [
        ("George Orwell", "British"),
        ("J.K. Rowling", "British"),
        ("Stephen King", "American"),
        ("Agatha Christie", "British"),
        ("Isaac Asimov", "American"),
        ("Jane Austen", "British")
    ]
    
    authors = []
    for name, nationality in authors_data:
        author = Author.create_author(name, nationality)
        authors.append(author)
    
    # Create books
    books_data = [
        ("1984", "978-0451524935", 1949, authors[0].id, genres[1].id, 4.7, 328),
        ("Animal Farm", "978-0451526342", 1945, authors[0].id, genres[0].id, 4.5, 112),
        ("Harry Potter and the Sorcerer's Stone", "978-0439708180", 1997, authors[1].id, genres[5].id, 4.8, 320),
        ("The Shining", "978-0307743657", 1977, authors[2].id, genres[0].id, 4.6, 447),
        ("Murder on the Orient Express", "978-0062693662", 1934, authors[3].id, genres[2].id, 4.4, 274),
        ("Foundation", "978-0553293357", 1951, authors[4].id, genres[1].id, 4.5, 255),
        ("Pride and Prejudice", "978-0141439518", 1813, authors[5].id, genres[3].id, 4.7, 432)
    ]
    
    for title, isbn, year, author_id, genre_id, rating, pages in books_data:
        Book.create_book(title, isbn, year, author_id, genre_id, rating, pages)
    
    print("Database seeded successfully!")

def validate_year(year_str):
    """Validate publication year input"""
    try:
        year = int(year_str)
        if 1000 <= year <= 2024:  # Reasonable year range
            return year
        else:
            print("Please enter a valid year between 1000 and 2024.")
            return None
    except ValueError:
        print("Please enter a valid year.")
        return None

def validate_rating(rating_str):
    """Validate rating input"""
    try:
        rating = float(rating_str)
        if 0 <= rating <= 5:
            return rating
        else:
            print("Please enter a rating between 0 and 5.")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None

def validate_pages(pages_str):
    """Validate pages input"""
    try:
        pages = int(pages_str)
        if pages > 0:
            return pages
        else:
            print("Please enter a positive number of pages.")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None
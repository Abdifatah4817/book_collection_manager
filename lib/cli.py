#!/usr/bin/env python3

from helpers import (
    exit_program, seed_database, validate_year, validate_rating, validate_pages
)
from models import Author, Genre, Book, session

def main():
    while True:
        print("\n" + "="*50)
        print("📚 BOOK COLLECTION MANAGER")
        print("="*50)
        print("1. Books  2. Authors  3. Genres  4. Seed Database  0. Exit")
        print("="*50)
        
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            manage_books()
        elif choice == "2":
            manage_authors()
        elif choice == "3":
            manage_genres()
        elif choice == "4":
            seed_database()
        else:
            print("Invalid choice.")

def manage_books():
    while True:
        print("\n📖 BOOKS: 1.View 2.Add 3.Search 4.Stats 0.Back")
        choice = input("> ")
        if choice == "0": break
        elif choice == "1": view_all_books()
        elif choice == "2": add_book()
        elif choice == "3": search_books()
        elif choice == "4": book_stats()
        else: print("Invalid choice.")

def manage_authors():
    while True:
        print("\n✍️ AUTHORS: 1.View 2.Add 3.Search 0.Back")
        choice = input("> ")
        if choice == "0": break
        elif choice == "1": view_all_authors()
        elif choice == "2": add_author()
        elif choice == "3": search_authors()
        else: print("Invalid choice.")

def manage_genres():
    while True:
        print("\n📚 GENRES: 1.View 2.Add 3.Search 0.Back")
        choice = input("> ")
        if choice == "0": break
        elif choice == "1": view_all_genres()
        elif choice == "2": add_genre()
        elif choice == "3": search_genres()
        else: print("Invalid choice.")

# Book functions
def view_all_books():
    books = Book.get_all_books()
    if not books:
        print("No books found.")
        return
    print(f"\n📚 {len(books)} Books:")
    for book in books:
        author = book.author.name if book.author else "Unknown"
        genre = book.genre.name if book.genre else "Unknown"
        print(f"ID:{book.id} | {book.title} | {author} | ⭐{book.rating}")

def add_book():
    print("\n➕ Add Book:")
    title = input("Title: ").strip()
    if not title: return print("Title required.")
    
    isbn = input("ISBN: ").strip()
    year = validate_year(input("Year: ").strip())
    if not year: return
    
    # Show available authors/genres
    authors = Author.get_all_authors()
    genres = Genre.get_all_genres()
    
    if not authors or not genres:
        return print("Add authors/genres first.")
    
    print("\nAuthors:"); [print(f"ID:{a.id} - {a.name}") for a in authors]
    author_id = input("Author ID: ").strip()
    if not Author.find_by_id(int(author_id)): return print("Invalid author.")
    
    print("\nGenres:"); [print(f"ID:{g.id} - {g.name}") for g in genres]
    genre_id = input("Genre ID: ").strip()
    if not Genre.find_by_id(int(genre_id)): return print("Invalid genre.")
    
    rating_str = input("Rating (0-5, optional): ").strip()
    rating = validate_rating(rating_str) if rating_str else 0.0
    
    try:
        book = Book.create_book(title, isbn, year, int(author_id), int(genre_id), rating)
        print(f"✅ Added: {book.title}")
    except Exception as e:
        print(f"Error: {e}")

def search_books():
    term = input("Search books by title: ").strip()
    books = Book.find_by_title(term)
    if books:
        print(f"\n🔍 Found {len(books)} books:")
        [print(f" - {b.title} by {b.author.name}") for b in books]
    else:
        print("No books found.")

def book_stats():
    books = Book.get_all_books()
    if not books: return print("No books.")
    
    total = len(books)
    avg_rating = sum(b.rating for b in books) / total
    print(f"\n📊 Stats: {total} books | Avg Rating: {avg_rating:.1f}")

# Author functions
def view_all_authors():
    authors = Author.get_all_authors()
    if not authors: return print("No authors.")
    print(f"\n✍️ {len(authors)} Authors:")
    for author in authors:
        print(f"ID:{author.id} | {author.name} | {author.nationality} | 📚{author.book_count}")

def add_author():
    print("\n➕ Add Author:")
    name = input("Name: ").strip()
    nationality = input("Nationality: ").strip()
    if name:
        author = Author.create_author(name, nationality)
        print(f"✅ Added: {author.name}")
    else:
        print("Name required.")

def search_authors():
    term = input("Search authors by name: ").strip()
    authors = Author.find_by_name(term)
    if authors:
        print(f"\n🔍 Found {len(authors)} authors:")
        [print(f" - {a.name} ({a.nationality})") for a in authors]
    else:
        print("No authors found.")

# Genre functions
def view_all_genres():
    genres = Genre.get_all_genres()
    if not genres: return print("No genres.")
    print(f"\n📚 {len(genres)} Genres:")
    for genre in genres:
        print(f"ID:{genre.id} | {genre.name} | 📚{genre.book_count}")

def add_genre():
    print("\n➕ Add Genre:")
    name = input("Name: ").strip()
    if name:
        genre = Genre.create_genre(name)
        print(f"✅ Added: {genre.name}")
    else:
        print("Name required.")

def search_genres():
    term = input("Search genres by name: ").strip()
    genres = Genre.find_by_name(term)
    if genres:
        print(f"\n🔍 Found {len(genres)} genres:")
        [print(f" - {g.name}") for g in genres]
    else:
        print("No genres found.")

if __name__ == "__main__":
    from models import Base, engine
    Base.metadata.create_all(engine)
    print("Welcome to Book Collection Manager!")
    main()
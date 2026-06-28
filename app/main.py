# print("Hello, World! <3")

from app.db.db import SessionLocal
from app.db.crud import get_categories, get_books

def main():
    db = SessionLocal()
    try:
        categories = get_categories(db)
        print("=== Категории ===")
        for cat in categories:
            print(f"ID: {cat.id}, Название: {cat.title}")

        print("\n=== Все книги ===")
        books = get_books(db)
        for book in books:
            print(f"{book.title} ({book.price} руб.) – категория: {book.category.title}")
    finally:
        db.close()

if __name__ == "__main__":
    main()
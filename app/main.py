import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.db import SessionLocal
from app.db.crud import get_categories, get_books
def main():
    db = SessionLocal()
    try:
        print("\n=== Категории ===")
        categories = get_categories(db)
        for cat in categories:
            print(f"ID: {cat.id}, Название: {cat.title}")

        print("\n=== Книги ===")
        books = get_books(db)
        for book in books:
            print(f"ID: {book.id}, Название: {book.title}, Цена: {book.price}, "
                  f"Категория ID: {book.category_id}, Описание: {book.description[:30]}...")
    finally:
        db.close()

if __name__ == "__main__":
    main()
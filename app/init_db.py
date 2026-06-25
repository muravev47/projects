import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.db import engine, SessionLocal
from app.db import models
from app.db.crud import create_category, create_book

def init_db():
    # Создаём таблицы, если их нет
    models.Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        # Добавляем категории
        categories_data = ["Фантастика", "Научпоп"]
        for cat_title in categories_data:
            # Проверяем, существует ли уже
            existing = db.query(models.Category).filter(models.Category.title == cat_title).first()
            if not existing:
                create_category(db, cat_title)

        # Получаем ID категорий
        fantasy_cat = db.query(models.Category).filter(models.Category.title == "Фантастика").first()
        science_cat = db.query(models.Category).filter(models.Category.title == "Научпоп").first()

        # Данные книг: (title, description, price, url, category_id)
        books_data = [
            ("Дюна", "Эпическая сага о пустынной планете", 15.99, "", fantasy_cat.id),
            ("Нейромант", "Классический киберпанк", 12.50, "", fantasy_cat.id),
            ("Игра Эндера", "Гениальный ребёнок в космической академии", 10.75, "", fantasy_cat.id),
            ("Краткая история времени", "Научно-популярная книга Стивена Хокинга", 18.20, "", science_cat.id),
            ("Sapiens", "Краткая история человечества", 22.30, "", science_cat.id),
        ]

        for title, desc, price, url, cat_id in books_data:
            existing_book = db.query(models.Book).filter(models.Book.title == title, models.Book.category_id == cat_id).first()
            if not existing_book:
                create_book(db, title, desc, price, url, cat_id)

        print("База данных успешно инициализирована.")
    except Exception as e:
        print(f"Ошибка при инициализации: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    init_db()
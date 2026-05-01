import psycopg2
from datetime import datetime
# Импортируем словарь настроек из вашего config.py
from config import config 

def connect():
    """Создает подключение к базе данных PostgreSQL, используя настройки из config.py."""
    try:
        conn = psycopg2.connect(**config)
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def parse_date(date_str):
    """
    Общая утилита для преобразования строки в объект даты.
    Используется и в phonebook.py, и в io_server.py.
    """
    if not date_str or not isinstance(date_str, str):
        return None
    try:
        # Пытаемся преобразовать строку формата ГГГГ-ММ-ДД
        return datetime.strptime(date_str.strip(), "%Y-%m-%d").date()
    except ValueError:
        print(f"Invalid date format: {date_str}. Expected YYYY-MM-DD.")
        return None
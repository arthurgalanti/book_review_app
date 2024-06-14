import sqlite3
from sqlite3 import Connection

def create_connection() -> Connection:
    connection = None
    try:
        connection = sqlite3.connect("book_review_app.db")
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return connection

def create_tables(connection: Connection):
    with connection:
        connection.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            );
        ''')
        connection.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                title TEXT NOT NULL,
                comment TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id)
            );
        ''')
        connection.execute('''
            CREATE TABLE IF NOT EXISTS sentiment_analysis (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                book_id INTEGER,
                sentiment TEXT,
                FOREIGN KEY (book_id) REFERENCES books(id)
            );
        ''')

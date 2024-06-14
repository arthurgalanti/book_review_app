from database.db_connection import create_connection
import hashlib

def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()

def create_user(username: str, password: str):
    connection = create_connection()
    with connection:
        connection.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hash_password(password)))

def get_user(username: str, password: str):
    connection = create_connection()
    with connection:
        user = connection.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, hash_password(password))).fetchone()
    return user

def user_exists(username: str) -> bool:
    connection = create_connection()
    with connection:
        result = connection.execute('SELECT 1 FROM users WHERE username = ?', (username,)).fetchone()
    return result is not None

def add_book(user_id: int, title: str, comment: str):
    connection = create_connection()
    with connection:
        connection.execute('INSERT INTO books (user_id, title, comment) VALUES (?, ?, ?)', (user_id, title, comment))

def delete_book(book_id: int):
    connection = create_connection()
    with connection:
        connection.execute('DELETE FROM books WHERE id = ?', (book_id,))

def get_books(user_id: int):
    connection = create_connection()
    with connection:
        books = connection.execute('SELECT * FROM books WHERE user_id = ?', (user_id,)).fetchall()
    return books

def add_sentiment_analysis(book_id: int, sentiment: str):
    connection = create_connection()
    with connection:
        connection.execute('INSERT INTO sentiment_analysis (book_id, sentiment) VALUES (?, ?)', (book_id, sentiment))

def get_sentiment_analysis(book_id: int):
    connection = create_connection()
    with connection:
        analysis = connection.execute('SELECT * FROM sentiment_analysis WHERE book_id = ?', (book_id,)).fetchone()
    return analysis

# main.py
from database.db_connection import create_connection, create_tables
from interfaces.pre_login_menu import pre_login_menu

def main():
    connection = create_connection()
    create_tables(connection)
    pre_login_menu()

if __name__ == "__main__":
    main()

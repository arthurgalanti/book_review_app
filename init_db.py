from database.db_connection import create_connection, create_tables

def initialize_database():
    connection = create_connection()
    create_tables(connection)
    print("Banco de dados inicializado.")

if __name__ == "__main__":
    initialize_database()

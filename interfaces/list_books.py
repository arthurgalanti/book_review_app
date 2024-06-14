from database.models import get_books
from database.models import get_sentiment_analysis
from utils.helpers import clear_console

def list_books(user_id):
    clear_console()
    print("=== Lista de Livros e Comentários ===")
    books = get_books(user_id)
    if not books:
        print("Nenhum livro encontrado.")
        input("Pressione Enter para voltar...")
        return
    
    for book in books:
        print(f"Título: {book[2]}")
        print(f"Comentário: {book[3]}")
        print("-" * 40)
    
    input("Pressione Enter para voltar...")

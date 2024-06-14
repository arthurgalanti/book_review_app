from database.models import get_books, delete_book as delete_book_entry
from utils.helpers import clear_console

def delete_book(user_id):
    clear_console()
    print("=== Excluir Livro ===")
    books = get_books(user_id)
    if not books:
        print("Nenhum livro encontrado.")
        input("Pressione Enter para voltar...")
        return
    
    for i, book in enumerate(books):
        print(f"{i + 1}. {book[2]}")
    
    while True:
        choice = input("Escolha o número do livro que deseja excluir (ou pressione Enter para cancelar): ")
        if choice == "":
            print("Operação cancelada.")
            break
        try:
            choice = int(choice) - 1
            if 0 <= choice < len(books):
                try:
                    delete_book_entry(books[choice][0])
                    print("Livro excluído com sucesso!")
                    break
                except Exception as e:
                    print(f"Erro ao excluir livro: {e}")
                    break
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
    input("Pressione Enter para voltar...")

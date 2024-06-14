from interfaces.add_book import add_book
from interfaces.delete_book import delete_book
from interfaces.analyze_sentiment import analyze_sentiment
from interfaces.list_books import list_books
from interfaces.export_analysis import export_analysis
from interfaces.import_analysis import import_analysis
from utils.helpers import clear_console

def post_login_menu(user_id):
    while True:
        clear_console()
        print("=== Menu Principal ===")
        print("1. Adicionar Livro")
        print("2. Excluir Livro")
        print("3. Listar Livros/Comentários")
        print("4. Analisar Sentimentos")
        print("5. Exportar Análises")
        print("6. Importar Análises")
        print("7. Logout")
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            add_book(user_id)
        elif choice == '2':
            delete_book(user_id)
        elif choice == '3':
            list_books(user_id)
        elif choice == '4':
            analyze_sentiment(user_id)
        elif choice == '5':
            export_analysis(user_id)
        elif choice == '6':
            import_analysis(user_id)
        elif choice == '7':
            print("Logout bem-sucedido.")
            break
        else:
            print("Opção inválida, tente novamente.")

from database.models import get_books, get_sentiment_analysis
from utils.helpers import clear_console

def analyze_sentiment(user_id):
    clear_console()
    print("=== Analisar Sentimentos ===")
    books = get_books(user_id)
    if not books:
        print("Nenhum livro encontrado.")
        input("Pressione Enter para voltar...")
        return
    
    for i, book in enumerate(books):
        print(f"{i + 1}. {book[2]}")
    
    while True:
        choice = input("Escolha o número do livro para ver a análise de sentimentos (ou pressione Enter para voltar):\n")
        if choice == "":
            print("Operação cancelada.")
            break
        try:
            choice = int(choice) - 1
            if 0 <= choice < len(books):
                analysis = get_sentiment_analysis(books[choice][0])
                if analysis:
                    print(f"Análise de Sentimento para '{books[choice][2]}': {analysis[2]}")
                else:
                    print("Nenhuma análise de sentimento encontrada.")
                break
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
    
    input("Pressione Enter para voltar...")

from database.models import get_books
from database.models import get_sentiment_analysis
from utils.helpers import clear_console
import json

def export_analysis(user_id):
    clear_console()
    print("=== Exportar Análise ===")
    books = get_books(user_id)
    if not books:
        print("Nenhum livro encontrado.")
        input("Pressione Enter para voltar...")
        return

    data = []
    for book in books:
        sentiment_analysis = get_sentiment_analysis(book[0])
        sentiment = sentiment_analysis[2] if sentiment_analysis else "N/A"
        data.append({
            "book": book[2],
            "comment": book[3],
            "sentiment_analysis": sentiment
        })

    filename = input("Digite o nome do arquivo (ex: analise.json): ")
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    
    print(f"Análise exportada com sucesso para {filename}.")
    input("Pressione Enter para voltar...")

from database.models import add_book, get_books, add_sentiment_analysis
from utils.helpers import clear_console
import json

def import_analysis(user_id):
    clear_console()
    print("=== Importar Análise ===")
    filename = input("Digite o nome do arquivo (ex: analise.json): ")
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        for item in data:
            add_book(user_id, item['book'], item['comment'])
            books = get_books(user_id)
            new_book = books[-1]
            add_sentiment_analysis(new_book[0], item['sentiment_analysis'])
        
        print("Análise importada com sucesso.")
    except Exception as e:
        print(f"Erro ao importar análise: {e}")
    
    input("Pressione Enter para voltar...")

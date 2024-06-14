import threading
import keyboard
from database.models import add_book as add_book_entry, get_books
from sentiment_analysis.analyze import gemini_analyze_sentiment
from database.models import add_sentiment_analysis
from utils.helpers import clear_console

cancel_flag = False

def monitor_escape():
    global cancel_flag
    cancel_flag = True
    print("\nOperação cancelada.")

def add_book(user_id):
    global cancel_flag
    cancel_flag = False
    
    clear_console()
    print("=== Adicionar Livro ===")
    print("Pressione ESC a qualquer momento para cancelar a operação.")

    keyboard.add_hotkey('esc', monitor_escape)

    try:
        while True:
            title = input("Título do Livro: ").strip()
            if cancel_flag:
                return
            if title:
                break
            print("O título do livro não pode estar vazio. Por favor, insira um título válido.")
        
        while True:
            comment = input("Comentário: ").strip()
            if cancel_flag:
                return
            if comment:
                break
            print("O comentário não pode estar vazio. Por favor, insira um comentário válido.")
        
        add_book_entry(user_id, title, comment)
        books = get_books(user_id)
        new_book = books[-1]
        sentiment = gemini_analyze_sentiment(title, comment)
        add_sentiment_analysis(new_book[0], sentiment)
        print("Livro adicionado com sucesso!")
        print(f"Análise de Sentimento: {sentiment}")
        input("Pressione Enter para voltar ao menu principal...")

    except Exception as e:
        print(f"Erro ao adicionar livro: {e}")
    finally:
        keyboard.unhook_all()

import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("A chave da API do Gemini não foi encontrada. Defina a variável de ambiente GEMINI_API_KEY.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-pro')

def gemini_analyze_sentiment(title: str, comment: str) -> str:
    try:
        prompt = f"Gere em uma linha a analise de sentimentos de sentimentos de livro: '{title}' esse comentário: '{comment}'"
        response = model.generate_content(prompt)
        sentiment = response.text
        return sentiment if sentiment else "Unknown"
    except Exception as e:
        print(f"Erro ao fazer chamada para a API do Gemini: {e}")
        return "Error"

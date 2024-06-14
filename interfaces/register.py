import threading
import keyboard
from database.models import create_user, user_exists
from utils.helpers import clear_console
import getpass

cancel_flag = False

def monitor_escape():
    global cancel_flag
    cancel_flag = True
    print("\nOperação cancelada.")

def register():
    global cancel_flag
    cancel_flag = False

    keyboard.add_hotkey('esc', monitor_escape)

    try:
        while True:
            clear_console()
            print("=== Registrar ===")
            print("Pressione ESC para cancelar...")

            username = input("Nome de usuário: ").strip()
            if cancel_flag:
                break
            if not username:
                print("O nome de usuário não pode estar vazio.\n")
                input("Pressione Enter para tentar novamente...")
                if cancel_flag:
                    break
                continue
            if user_exists(username):
                print("Nome de usuário já existe. Por favor, escolha outro nome.\n")
                input("Pressione Enter para tentar novamente...")
                if cancel_flag:
                    break
                continue

            password = getpass.getpass("Senha: ").strip()
            if cancel_flag:
                break

            if not password:
                print("A senha não pode estar vazia.\n")
                input("Pressione Enter para tentar novamente...")
                if cancel_flag:
                    break
                continue

            try:
                create_user(username, password)
                print("Usuário registrado com sucesso!\n")
                break
            except Exception as e:
                print(f"Erro ao registrar usuário: {e}")
                if cancel_flag:
                    break
                print("Pressione Enter para tentar novamente ou ESC para cancelar...")
                input()
                if cancel_flag:
                    break
    finally:
        keyboard.unhook_all()

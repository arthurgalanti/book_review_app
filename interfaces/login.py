import threading
import keyboard
from database.models import get_user
from interfaces.post_login_menu import post_login_menu
from utils.helpers import clear_console
import getpass

cancel_flag = False

def monitor_escape():
    global cancel_flag
    cancel_flag = True
    print("\nOperação cancelada.")

def login():
    global cancel_flag
    cancel_flag = False

    keyboard.add_hotkey('esc', monitor_escape)

    try:
        while True:
            clear_console()
            print("=== Login ===")
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

            password = getpass.getpass("Senha: ").strip()
            if cancel_flag:
                break

            if not password:
                print("A senha não pode estar vazia.\n")
                input("Pressione Enter para tentar novamente...")
                if cancel_flag:
                    break
                continue

            user = get_user(username, password)
            if user:
                print("Login bem-sucedido!")
                post_login_menu(user[0])
                break
            else:
                print("Nome de usuário ou senha incorretos.\n")
                if cancel_flag:
                    break
                print("Pressione Enter para tentar novamente ou ESC para cancelar...")
                input()
                if cancel_flag:
                    break
    finally:
        keyboard.unhook_all()

from interfaces.register import register
from interfaces.login import login
from interfaces.about import about
from utils.helpers import clear_console

def pre_login_menu():
    while True:
        clear_console()
        print("Bem-vindo ao Book Review App")
        print("1. Registrar")
        print("2. Login")
        print("3. Sobre")
        print("4. Sair")
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            about()
        elif choice == '4':
            print("Saindo...")
            clear_console()

            break
        else:
            print("Opção inválida, tente novamente.")
            input("Pressione Enter para continuar...")

from interfaces.main_menu import menu
from db.connection import get_connection

def main() -> None:
    # try:
    #     conn = get_connection('localhost', 'root', 'proads.2024', 'biblioteca')
    # except Exception as e:
    #     print(e)

    menu('Gestion Biblioteca')

if (__name__ == '__main__'):
    main()

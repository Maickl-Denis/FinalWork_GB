import os
from FinalWork_GB.Resource import DB_Handler
from FinalWork_GB.menu import menu


def check_db(name_db):
    print(f"[!] Проверяем существует ли БД {name_db}")
    if not os.path.isfile(name_db):
        print(f"БД {name_db} не наедена, приступаю к созданию")
        DB_Handler.create_db(name_db)
        print("Приступаю к наполнению БД данными...")
    else:
        print(f"[+] БД {name_db} существвет, приступаю к работе.")


if __name__ == '__main__':
    name_bd_file = DB_Handler.Name_db()
    name_bd_file.name_db = 'database.db'

    check_db(name_bd_file.name_db)
    menu()

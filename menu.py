import os

from FinalWork_GB.Model.Cat import Cat
from FinalWork_GB.Model.Dog import Dog
from FinalWork_GB.Model.Hamster import Hamster
from FinalWork_GB.Resource.DB_Handler import inmput_animal, getAnimal, update_command


def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        num, men = first_menu()
        match num:
            # 1. Завести новое животное
            case 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                num1, men = new_animal()
            # 2. Список всех животных
            case 2:
                getAnimal()
                input("Для продолжения работы нажмите на любую кнопку")
            case 3:
                less_animal()
            case 0:
                break


def first_menu():
    try:
        ls = {1: "Завести новое животное", 2:"Список всех животных", 3:"Научить животное новой команде", 0: "Выход"}
        num = int(input(f"Реестр домашних животных\n"
                        f"1. {ls[1]}\n"
                        f"2. {ls[2]}\n"
                        f"3. {ls[3]}\n"
                        f"0. {ls[0]}\n"
                        "Выберете пункт меню:  "))
    except ValueError:
        return -1, None
    else:
        return num, ls.get(num)


def new_animal():
    try:
        ls = {1: "Собака", 2: "Кошка", 3: "Хомячек", 0: "Выход"}
        ls2 = {"Собака": Dog(), "Кошка": Cat(), "Хомячек": Hamster()}
        typy_anim = int(input(f"Выберети какое животное хотите добавить в реестр\n"
                        f"1. {ls[1]}\n"
                        f"2. {ls[2]}\n"
                        f"3. {ls[3]}\n"
                        f"0. {ls[0]}\n"
                        "Выберете пункт меню:  "))
        anim = ls2[ls.get(typy_anim)]
        name = input(f"Введите имя {ls.get(typy_anim)}: ")
        anim.set_name(name)
        birthday = input(f"Ведите дату в формате ГГГГ-ММ-ДД\n")
        anim.set_birthday(birthday)

        if anim.get_name() and anim.get_birthday():
            inmput_animal(ls2[ls.get(typy_anim)], typy_anim)

        else:
            print("[-] В данных ошибка")

    except ValueError:
        return -1, None
    except KeyError:
        return -1, None
    else:
        return typy_anim, ls.get(typy_anim)

def less_animal():
    try:
        ls = {1: "Собака", 2: "Кошка", 3: "Хомячек", 0: "Выход"}
        ls2 = {"Собака": "dogs", "Кошка": "cats", "Хомячек": "hamsters"}
        typy_anim = int(input("Какие животные вы хотите научить\n"
                        f"1. {ls[1]}\n"
                        f"2. {ls[2]}\n"
                        f"3. {ls[3]}\n"
                        f"0. {ls[0]}\n"
                        "Выберете пункт меню:  "))
        getAnimal(anima=ls2[ls.get(typy_anim)], idTrue=False)
        id_anima = int(input("Выбор животного (введите id): "))
        lessen = input("Введите команду которой вы хотите научить животное\n")
        update_command(anima=ls2[ls.get(typy_anim)], id=id_anima, new_comand=lessen)

    except ValueError:
        return -1, None
    except KeyError:
        return -1, None
    else:
        return typy_anim, ls.get(typy_anim)



if __name__ == '__main__':
    menu()

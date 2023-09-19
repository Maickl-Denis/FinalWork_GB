import sqlite3


class Name_db:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state
        if not self._shared_state:
            self.name_db = 'database.db'

    def get_name(self):
        return self._shared_state


def create_db(name_db):
    try:
        sqlite_connection = sqlite3.connect(str(name_db))

        sqlite_create_table_animal = '''CREATE TABLE IF NOT EXISTS animal(
                                        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                        class_name VARCHAR(30));'''

        sqlite_create_home_animals = '''CREATE TABLE IF NOT EXISTS home_animals(
                                        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                                        type_name VARCHAR (20), 
                                        animal_id INT, 
                                        FOREIGN KEY (animal_id) REFERENCES animal (id) ON DELETE CASCADE ON UPDATE CASCADE);'''

        sqlite_create_table_pack_animals = '''CREATE TABLE IF NOT EXISTS pack_animals(
                                        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                                        type_name VARCHAR (20), 
                                        animal_id INT, 
                                        FOREIGN KEY (animal_id) REFERENCES animal (id) ON DELETE CASCADE ON UPDATE CASCADE);'''

        sqlite_create_table_dogs = '''CREATE TABLE IF NOT EXISTS dogs(
                                      id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                                      name VARCHAR(20), 
                                      birthday DATE, 
                                      commands VARCHAR(50), 
                                      type_id int, 
                                      Foreign KEY (type_id) REFERENCES home_animals (id) ON DELETE CASCADE ON UPDATE CASCADE);'''

        sqlite_create_table_cats = '''CREATE TABLE IF NOT EXISTS cats(
                                      id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                      name VARCHAR(20), 
                                      birthday DATE, 
                                      commands VARCHAR(50), 
                                      type_id int, 
                                      Foreign KEY (type_id) REFERENCES home_animals (id) ON DELETE CASCADE ON UPDATE CASCADE);'''

        sqlite_create_table_hamsters = '''CREATE TABLE IF NOT EXISTS hamsters(
                                          id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                          name VARCHAR(20), 
                                          birthday DATE, 
                                          commands VARCHAR(50), 
                                          type_id int, 
                                          Foreign KEY (type_id) REFERENCES home_animals (id) ON DELETE CASCADE ON UPDATE CASCADE);'''

        sqlite_create_table_horses = '''CREATE TABLE IF NOT EXISTS horses(
                                      id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                      name VARCHAR(20), 
                                      birthday DATE, 
                                      commands VARCHAR(50), 
                                      type_id int, 
                                      Foreign KEY (type_id) REFERENCES home_animals (id) ON DELETE CASCADE ON UPDATE CASCADE);'''

        sqlite_create_table_Camel = '''CREATE TABLE IF NOT EXISTS Camel(
                                      id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                      name VARCHAR(20), 
                                      birthday DATE, 
                                      commands VARCHAR(50), 
                                      type_id int, 
                                      Foreign KEY (type_id) REFERENCES home_animals (id) ON DELETE CASCADE ON UPDATE CASCADE);'''

        sqlite_create_table_Donkey = '''CREATE TABLE IF NOT EXISTS Donkey(
                                      id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                      name VARCHAR(20), 
                                      birthday DATE, 
                                      commands VARCHAR(50), 
                                      type_id int, 
                                      Foreign KEY (type_id) REFERENCES home_animals (id) ON DELETE CASCADE ON UPDATE CASCADE);'''

        sqlite_inData_table_animal = '''INSERT INTO animal
                                      (class_name)
                                      VALUES ('Домашние'), ('Вьючные');'''

        sqlite_inData_pack_animals = '''INSERT INTO pack_animals
                                    (type_name, animal_id) 
                                    VALUES ('Лошади', 2), ('Верблюды', 2), ('Ослы', 2);'''

        sqlite_inData_home_animals = '''INSERT INTO home_animals
                                    (type_name, animal_id) 
                                    VALUES ('Собаки', 1), ('Кошки', 1), ('Хомячки', 1);'''

        sqlite_inData_dogs = '''INSERT INTO dogs
                                (name, birthday, commands, type_id) 
                                VALUES 
                                ('Лана', '2022-06-01', 'к ноге, лежать, сидеть, голос', 1), 
                                ('Шарик', '2022-06-02', "сидеть, лежать, лапу, принеси", 1), 
                                ('Полкан', '2022-06-03', "сидеть, лежать, лапу, фас", 1), 
                                ('Рэй', '2022-06-04', "сидеть, лежать, голос, место", 1);'''

        sqlite_inData_cats = '''INSERT INTO cats
                                (name, birthday, commands, type_id) 
                                VALUES 
                                ('Киса', '2022-06-05', 'есть', 2), 
                                ('Муркзик', '2022-06-06', 'умри', 2);'''

        sqlite_inData_hamsters = '''INSERT INTO hamsters
                                (name, birthday, commands, type_id) 
                                VALUES 
                                ('Лео', '2022-06-06', NULL, 3), 
                                ('Донатело', '2022-06-07', NULL, 3), 
                                ('Микеланджело', '2022-06-08', "", 3);'''

        sqlite_inData_horses = '''INSERT INTO horses
                                (name, birthday, commands, type_id) 
                                VALUES 
                                ('Звездачка', '2022-06-09', 'Голоп', 1), 
                                ('Искорка', '2022-06-10', 'Рысь', 1), 
                                ('Задира', '2022-06-11', "Сбросить наездника", 1);'''

        sqlite_inData_Camel = '''INSERT INTO Camel
                                (name, birthday, commands, type_id) 
                                VALUES 
                                ('Верблюд 1', '2022-06-12', 'сбросить горб', 2), 
                                ('Верблюд 2', '2022-06-13', 'убить всех людей', 2), 
                                ('Верблюд 3', '2022-06-14', "Найти воду", 2);'''

        sqlite_inData_Donkey = '''INSERT INTO Donkey
                                (name, birthday, commands, type_id) 
                                VALUES 
                                ('Осел 1', '2022-06-15', 'Тащить груз', 3), 
                                ('Осел 2', '2022-06-16', 'Тащить груз больше чем соседний осел', 3), 
                                ('Осел 3', '2022-06-15', "Везти человека", 3);'''

        cursor = sqlite_connection.cursor()
        print(f"[+] База данных {name_db} создана")

        cursor.execute(sqlite_create_table_animal)
        cursor.execute(sqlite_create_home_animals)
        cursor.execute(sqlite_create_table_pack_animals)
        cursor.execute(sqlite_create_table_dogs)
        cursor.execute(sqlite_create_table_cats)
        cursor.execute(sqlite_create_table_hamsters)
        cursor.execute(sqlite_create_table_horses)
        cursor.execute(sqlite_create_table_Camel)
        cursor.execute(sqlite_create_table_Donkey)
        cursor.execute(sqlite_inData_table_animal)
        cursor.execute(sqlite_inData_pack_animals)
        cursor.execute(sqlite_inData_home_animals)
        cursor.execute(sqlite_inData_dogs)
        cursor.execute(sqlite_inData_cats)
        cursor.execute(sqlite_inData_hamsters)
        cursor.execute(sqlite_inData_horses)
        cursor.execute(sqlite_inData_Camel)
        cursor.execute(sqlite_inData_Donkey)

        sqlite_connection.commit()
        print("[+] Созданы таблицы")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error, "create_db")
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("[-] Соединение с SQLite закрыто")


def inmput_animal(anim, type_anim):
    nameBD = Name_db().get_name()
    try:
        connectSQL = sqlite3.connect(nameBD["name_db"])
        cursor = connectSQL.cursor()

        insert_data = f"""INSERT INTO {anim.getAnimalType()}s
                        (name, birthday, type_id)
                        VALUES(?, ?, ?);"""

        val_data = (anim.get_name(), anim.get_birthday(), type_anim)

        cursor.execute(insert_data, val_data)
        connectSQL.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error, "__AddInDB")
    finally:
        print("Запись создана")
        if connectSQL:
            connectSQL.close()


def getAnimal(anima="all", idTrue=True):
    nameBD = Name_db().get_name()
    try:
        connectSQL = sqlite3.connect(nameBD["name_db"])
        cursor = connectSQL.cursor()

        if anima == "all":
            requestSQL = """SELECT c.name, c.birthday, c.commands, ha.type_name
                            FROM cats c
                            LEFT JOIN home_animals ha ON ha.id = c.type_id
                            UNION
                            SELECT d.name, d.birthday, d.commands, ha.type_name
                            FROM dogs d
                            LEFT JOIN home_animals ha ON ha.id = d.type_id
                            UNION
                            SELECT hm.name, hm.birthday, hm.commands, ha.type_name
                            FROM hamsters hm
                            LEFT JOIN home_animals ha ON ha.id = hm.type_id;"""
        else:
            requestSQL = f"""SELECT c.id, c.name, c.birthday, c.commands, ha.type_name
                                        FROM {anima} c
                                        LEFT JOIN home_animals ha ON ha.id = c.type_id;"""
        cursor.execute(requestSQL)
        result = cursor.fetchall()

        cursor.close()
        title = f"{'id':<3}{'Имя':<15}{'дата рождения':<15}{'Вид':<10}{'Команды'}"

        print(title)
        if idTrue:
            counter = 1
            for row in result:
                print(f'{counter:<3}{row[0]:<15}{row[1]:<15}{row[3]:<10}{row[2]}')
                counter += 1
        else:
            for row in result:
                print(f'{row[0]:<3}{row[1]:<15}{row[2]:<15}{row[4]:<10}{row[3]}')

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error, "__getValForDB")
    finally:
        if connectSQL:
            connectSQL.close()

def update_command(anima, id, new_comand):
    nameBD = Name_db().get_name()
    try:
        connectSQL = sqlite3.connect(nameBD["name_db"])
        cursor = connectSQL.cursor()

        requestSQL = f"""SELECT commands
                         FROM {anima}
                         WHERE id = {id};"""
        cursor.execute(requestSQL)
        result = cursor.fetchall()
        result = result[0][0]
        if result:
            result = result+", "+new_comand
        else: result = new_comand

        requestSQL = f"""UPDATE {anima} SET commands = ? WHERE id = ?;"""
        data = (result, id)
        cursor.execute(requestSQL, data)
        connectSQL.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error, "update_command")
    finally:
        if connectSQL:
            connectSQL.close()


if __name__ == '__main__':
    pass
    # nameBD = Name_db().get_name()
    # connectSQL = sqlite3.connect(r"G:\gb\final work\FinalWork_GB\database.db")
    # cursor = connectSQL.cursor()
    #
    # requestSQL = """select * from cats"""
    # cursor.execute(requestSQL)
    # result = cursor.fetchall()
    #
    # cursor.close()
    #
    # print(result[0] if result else False)

import datetime


class Animal:
    def __init__(self):
        self.__pet_id = None
        self.__name = None
        self.__birthday = None
        self.__lessen = None

    def set_pet_id(self, pet_id):
        self.__pet_id = pet_id

    def get_pet_id(self):
        return self.__pet_id

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_birthday(self, birthdate):

        try:
            birthdate = datetime.datetime.strptime(birthdate, '%Y-%m-%d')
            self.__birthday = birthdate.strftime("%Y-%m-%d")
        except ValueError:
            print("Неверный формат даты")


    def get_birthday(self):
        return self.__birthday

    def set_lessen(self, less):
        self.__lessen = str(less)

    def get_lessen(self):
        return self.__lessen

    def __str__(self):
        return f"Питомец с идентификатором {self.__pet_id}: имя: {self.__name}, дата рождения: {self.__birthday}"


# if __name__ == '__main__':

    # pet1 = Animal()
    # pet1.set_birthday("2022-06-06")
    # pet1.set_pet_id(1)
    # pet1.set_name("Шарик")
    # print(pet1)
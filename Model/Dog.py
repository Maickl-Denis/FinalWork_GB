from FinalWork_GB.Model.AnymalType import AnimalType
from FinalWork_GB.Model.Home_animals import Home_animals

class Dog(Home_animals):
    def __init__(self):
        super().__init__()
        self.__AnimalType = AnimalType(1).AnimalType()



    def getAnimalType(self):
        return self.__AnimalType


    def __str__(self):
        return f"{self.__AnimalType} с идентификатором {self.get_pet_id()}: имя: {self.get_name()}, дата рождения: {self.get_birthday()}"
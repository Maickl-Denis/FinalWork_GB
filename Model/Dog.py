from FinalWork_GB.Model.AnymalType import AnimalType
from FinalWork_GB.Model.Home_animals import Home_animals

class Dog(Home_animals):
    def __init__(self):
        super().__init__()
        self.__AnimalType = AnimalType(1).AnimalType()



    def getAnimalType(self):
        return self.__AnimalType
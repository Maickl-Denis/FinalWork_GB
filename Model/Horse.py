from FinalWork_GB.Model.AnymalType import AnimalType
from FinalWork_GB.Model.Pack_animals import Pack_animals


class Horse(Pack_animals):
    def __init__(self):
        super().__init__()
        self.__AnimalType = AnimalType(4).AnimalType()



    def getAnimalType(self):
        return self.__AnimalType

from FinalWork_GB.Model.AnymalType import AnimalType
from FinalWork_GB.Model.Home_animals import Home_animals


class Cat(Home_animals):
    def __init__(self):
        super().__init__()
        self.__AnimalType = AnimalType(2).AnimalType()



    def getAnimalType(self):
        return self.__AnimalType


if __name__ == '__main__':
    d = Cat()
    print(d)
    print(d.getAnimalType())
    print(d.getViewAnimalType())
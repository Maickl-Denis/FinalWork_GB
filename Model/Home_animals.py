from FinalWork_GB.Model.Animal import Animal

class Home_animals(Animal):
    def __init__(self):
        super().__init__()
        self.__ViewAnimalType = 'Домашние'

    def getViewAnimalType(self):
        return self.__ViewAnimalType
from FinalWork_GB.Model.Animal import Animal

class Pack_animals(Animal):
    def __init__(self):
        super().__init__()
        self.__ViewAnimalType = 'Вьючные'

    def getViewAnimalType(self):
        return self.__ViewAnimalType
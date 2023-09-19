class AnimalType:
    def __init__(self, typeId):
        self.typeId = typeId
    def AnimalType(self):
        match self.typeId:
            case 1:
                return 'Dog'
            case 2:
                return 'Cat'
            case 3:
                return "Hamster"
            case 4:
                return "Horse"
            case 5:
                return "Camel"
            case 6:
                return "Donkey"
            case _:
                return None


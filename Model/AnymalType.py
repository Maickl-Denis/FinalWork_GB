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
            case _:
                return None


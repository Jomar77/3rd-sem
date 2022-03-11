class vehicle:
    def __init__(self,type):
        self._type = type

    def getType(self):
        return self._type

class landVehicle(vehicle):
    def __init__(self,type):
        super().__init__(type)

class Auto(landVehicle):
    def __init__(self,type):
        super().__init__(type)

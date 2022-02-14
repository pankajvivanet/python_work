
class Vehical:
    def __init__(self, vehical_name):
        print("Name=", vehical_name)
    
    def Vehical_info(self, vehival_name):
        print("Vehical info", vehival_name, self.company)

class Car(Vehical):
    def __init__(self, vehical_name):
        super().Vehical_info(vehical_name)
    
car = Car("Car")
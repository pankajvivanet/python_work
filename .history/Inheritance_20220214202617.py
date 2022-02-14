
class Vehical:
        
    def Vehical_info(self, vehival_name):
        print("Vehical info", vehical_name)

class Car(Vehical):
    vehical_name = ""
    def __init__(self, vehical_name):
        self.vehical_name = vehical_name
        
    super().Vehical_info(vehical_name)

car = Car("Car")
class Vehical:
    def info(self):
        print("This is Vehical")

class Car(Vehical):
    def car_info(self):
        print("In Car calss")

class Truck(Vehical):
    def truck_info(self):
        print("In Truck calss")

class SportCar(Car, Truck, Vehical):
    def sportcar_info(self):
        print("In Sprot calss")        

class Vehical:
    def info(slef):
        print("This is Vehical")

class Car(Vehical):
    def car_info(slef, name):
        print("Car name is = ", name)

class Truck(Vehical):
    def truck_info(self, name):
        print("Truck name is = ", name)

obj1 = Car()
obj1.car_info("BMW")
obj1.info()
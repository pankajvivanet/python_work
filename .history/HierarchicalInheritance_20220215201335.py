class Vehical:
    def info(self):
        print("This is Vehical")

class Car(Vehical):
    def car_info(self, name):
        print("Car name is = ", name)

class Truck(Vehical):
    def truck_info(self, name):
        print("Truck name is = ", name)

obj1 = Car()
obj1.car_info("BMW")
obj1.info()

obj2 = Truck()
obj2.info()
obj2.truck_info("Ford")

class Vehical:
    def __init__(self):
        print("In Parent class")
    
    def vehical_into(self):
         print("In parent class")
    
class Car(Vehical):
    def __init__(self):
        print("Name in car subcalss")
    
    def car_into(self):
         print("In sub class")
                
class SprotCar(Car):
    def __init__(self):
        #print("In Sub sub class")
    
    def sport_car_into(self):
         print("In Sub sub class")

s_car= SprotCar()
s_car.sport_car_into()
s_car.car_into()
s_car.vehical_into()
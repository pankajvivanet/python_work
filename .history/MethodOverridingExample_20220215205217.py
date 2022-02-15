from difflib import SequenceMatcher
from turtle import Shape


class Vehical:
    def speed(self):
        print("Vehical max speed is 100km/hr")
        
class Car(Vehical):
    def speed(self):
        print("car max speed is 200 km/hr")
        
car = Car()
car.speed()

'''
Shape -> draw()
|
Cricle --> draw()
Square --> draw()
Tringle --> draw()'''
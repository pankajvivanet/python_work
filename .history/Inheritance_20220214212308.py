#Example of Simple inheritance
class Vehical:
    def __init__(self, vehical_name):
        print("Name=", vehical_name)
    
    def Vehical_info(self, vehival_name):
        print("Vehical info", vehival_name)
        
class Car(Vehical):
    def __init__(self, vehical_name):
        print("Name in subcalss=", vehical_name)
        #super().__init__(vehical_name)
        super().Vehical_info(vehical_name)
    
car = Car("Tata")

#Example of multiple inheritance
class Vehical:
    def __init__(self, vehical_name):
        print("Name=", vehical_name)
    
    def Vehical_info(self, vehival_name):
        print("Vehical info", vehival_name)

class Company:
    def __init__(self, company_name):
        print("Company name=", company_name)
        
    def company_info(self, company_name):
        print("Car info", company_name)
        
class Car(Company, Vehical):
    def __init__(self, vehical_name):
        #vehical_name = "Tata"
        print("Name in subcalss=", vehical_name)
        #super().__init__(vehical_name)
        super().company_info(vehical_name)
        super().Vehical_info(vehical_name)
    
car = Car("Tata")
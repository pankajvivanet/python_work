
class Vehical:
    def __init__(self, vehical_name):
        print("Name=", vehical_name)
    
    def Vehical_info(self, vehival_name):
        print("Vehical info", vehival_name)

class Company:
    def __init__(self, company_name):
        print("Company name=", company_name)
        
class Car(Company):
    pass
    '''def __init__(self, vehical_name):
        print("Name in subcalss=", vehical_name)
        super().__init__(vehical_name)'''
    
car = Car("Tata")
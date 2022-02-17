#public member
#private
#protected
'''
class Employee:
    def __init__(self, name, salary):
        #public members
        self.name = name
        self.salary = salary
    
    def show(self):
        #public data memebers
        print("Name= ", self.name, " Salary = ", self.salary)

emp = Employee("Akash", 10000)

print("Name = ", emp.name, " Salary = ", emp.salary)
#calling public method
emp.show()'''


class Employee:
    def __init__(self, name, salary):
        #public members
        self.name = name
        self.__salary = salary
    
    #def show(self):
        #public data memebers
        #print("Name= ", self.name, " Salary = ", self.salary)

emp = Employee("Akash", 10000)

print("Name = ", emp.name, " Salary = ", emp.__salary)

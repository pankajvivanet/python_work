#public member None
#private __
#protected _
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
'''
#Private data members
class Employee:
    def __init__(self, name, salary):
        #public members
        self.name = name
        #private data member
        self.__salary = salary
    
    def show(self):
        #public data memebers
        print("Name= ", self.name, " Salary = ", self.__salary)

emp = Employee("Akash", 10000)
print("Name = ", emp.name, " Salary = ", emp._Employee__salary)
emp.show()
'''
'''
#Protected
class Company:
    def __init__(self) :
        self._project = "Python"

class Employee(Company):
    def __init__(self, name):
        self.name = name
        Company.__init__(self)
        
    def __show(self):
        print("Employee = ", self.name, " Working on project = ", self._project)
        
    def callShow(self):
        self.__show()
        
emp = Employee("Pankaj")
emp.callShow()
#print("Project Name=", emp._project)        '''


class Employee:
    
    def __init__(self, name, salary):
        #public members
        self.name = name
        self.__salary = salary
        
    def getSalary(self):
        return self.__salary

emp = Employee("Akash", 10000)
print("Salary =",emp.getSalary())

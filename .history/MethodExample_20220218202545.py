#Instance - call using class object + slef
#Class - call using ClassName as well as using object + cls
#Static - clas name + non


'''
class Employee:
    def __init__(self, name, salary):
        #public members
        self.name = name
        self.salary = salary
        
    def showEmployee(self):
        print("Name = ", self.name," Salary= ", self.salary)
        
emp = Employee("Akash", 10000)
emp.showEmployee()
'''
class Employee:
    company_name = "ABC Corp"
    def __init__(self, name, salary):
        #public members
        self.name = name
        self.salary = salary
        
    def show(self):
        print("Name = ", self.name," Salary= ", self.salary)
        
    @classmethod
    def showEmployee(cls, name, salary):
        Employee.show()
        print("Name = ", name," Salary= ", salary, "Company Name=", Employee.company_name)
        
#emp = Employee("Akash", 10000)

Employee.showEmployee("Akash", 10000)

#emp.showEmployee()


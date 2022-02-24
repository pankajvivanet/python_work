class Employee:
    def __init__(self, name, salary):
        #public members
        self.name = name
        self.salary = salary
        
    def getSalary(self):
        return self.salary
    
    def setSalary(self, salary):
        self.salary = salary

emp = Employee("Akash", 10000)
emp.setSalary(20000)
print("Salary =",emp.getSalary())

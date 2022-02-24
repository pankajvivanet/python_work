class Employee:
    def __init__(self, name, salary):
        #public members
        self.name = name
        self.salary = salary
        
    def showEmployee(self):
        print("Name = ", self.name," Salary= ", self.salary)
        
emp = Employee("Akash", 10000)
emp.setSalary(20000)
print("Salary =",emp.getSalary())

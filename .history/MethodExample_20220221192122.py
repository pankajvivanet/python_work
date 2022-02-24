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

class Employee:
    company_name = "ABC Corp"
    def __init__(self, name, salary):
        #public members
        self.name = name
        self.salary = salary
        
    def show(self):
        self.company_name
        print("Name = ", self.name," Salary= ", self.salary)
        
    @classmethod
    def showEmployee(cls, name, salary):        
        print("Name = ", name," Salary= ", salary, "Company Name=", Employee.company_name)
        
Employee.showEmployee("Akash", 10000)
emp_1 = Employee("Akash", 10000)
emp_2 = Employee("Akash_1", 20000)
emp_3 = Employee("Akash_2", 30000)

print(emp_3.company_name)
'''
'''
class Employee: 
    company_name = "ABC Corp"
    
    def __init__(self) -> None:
        self.name = "xyz"
    
    @staticmethod
    def showEmployee(x):
        print("In static method",x)
        
Employee.showEmployee(10)

emp = Employee()
emp.showEmployee(10)

# Function / Method
'''

nums = []
vals = nums[:]
vals.append(1)
print(len(vals))
print(len(nums))






        

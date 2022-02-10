"""employee={"name":"Smith", "age":40, "salaray":40000, "company":"Unicon"}
print(type(employee))
print("Display Employee data= \n", employee)

new_employee=dict({"name":"Smith", "age":40, "salaray":40000, "company":"Unicon"})

print("Display new emplyee data=\n", new_employee)

dict1 = dict({1:"Java", 2:"Python", 3:"C", 4:"VB"})
print("dict1 data =\n", dict1)

#Get the data from Disc
employee={"name":"Smith", "age":40, "salaray":40000, "company":"Unicon"}

print("Display employee data ")
print("Name:%s" %employee["name"])
print("Age:%d" %employee["age"])
print("Salary:%d" %employee["salaray"])

#Add new data in dict
#employee={"name":"Smith", "age":40, "salaray":40000, "company":"Unicon"}
dict1={}
print("Empty Dict.=\n", dict1)
dict1[0]="Pitter"
dict1["age"]=50
dict1["Salary"]=15000,30000,50000
print("Dict1 data=\n", dict1)


employee={"name":"Smith", "age":40, "salaray":40000, "company":"Unicon"}
print("Employee data =\n", employee)

print("Take input from user to add new employee = ")
#employee["name"] = input("Enter the name of employee")
#employee["age"]=int(input("Enter the age of employee"))
#employee["salaray"] = int(input("Enter the salary"))
#employee["company"] = input("Enter the company name")

#print("Employee data again = \n", employee)

#delete 
del employee["name"]
print("Delete data=\n",employee)
del employee["age"]
print(employee)
#del employee
#print("Empty =\n", employee)

employee.pop("company")
print("Remaining employee data=\n", employee)

employee={"name":"Smith", "age":40, "salaray":40000, "company":"Unicon"}
for x in employee:
    print(x)
print()
for x in employee:
    print(employee[x])
print()
for x in employee.items():
    print(x)

print()
for x, y in employee.items():
    print(x,y)
"""
from filecmp import cmp


employee={"name":"Smith", "age":40, "salaray":40000, "company":"Unicon"}
print("Length=", len(employee))

employee1={"name":"John", "age":50, "salaray":50000, "company":"Apple"}
#print("Compare data=", cmp(str(employee), str(employee1)))

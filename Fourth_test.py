#functions
'''
def my_first_function():
    print("Hello in function")
    
#my_first_function()


def parameter_function(number):
    print("in function", number)
    
#parameter_function(number=5)  

def myself(first_name, last_name):
    print("Hello my name =", first_name, last_name)

#myself(last_name="Tom", first_name="Larry")

def myself_gain(first_name, last_name="Smith"):
    print("Hello my name =", first_name, last_name)
    
myself_gain("Will")
myself_gain("Will", "Larry")


def myself_onemore_time(first_name, last_name="Smith", middle_name="M"):
    print("Hello my name =", first_name, middle_name, last_name)
    
myself_onemore_time("Will")
myself_onemore_time("Will", "M", "Larry")


def my_first_function():
    print("Hello in function")
    return 123
    
x = my_first_function()
print("return value", x)

value = 4
if value == 4:
    print("There is value")

value = None
if value is None:
    print("There is no value")
'''

def new_function(n):
    print("#1 value of n = ",n)
    n=10
    print("#2 value of n = ",n)

n=1
new_function(n)
print("#3 value of n = ",n)

print("-------")


def new_function_1():
    global n
    print("#1 value of n = ",n)
    n=10
    print("#2 value of n = ",n)

n=1
new_function_1()
print("#3 value of n = ",n)



assignement - write a function which evalutae leap year
function will take param as input year value return true or False
year value should pass to function from any loop (for / while)

year_list = (1990 , ,,2025)






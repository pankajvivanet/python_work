'''student=["Akash", "Harshad", "Gauri"]
college= "ABC college"

print(len(student))
print(len(college))'''

#Exaple of overriding default built in method
class Example:
    def __init__(self, basket):
        self.basket = list(basket)
    
    def __len__(self):
        val = len(self.basket)
        print("Value=", val)
        return val

example = Example(['Glasses','TShirt'])
print(len(example))


#Overloading
'''
the process of calling the same method with different parameters is called as method overloading but 
python does not support that one as Python consider only the latest define method in its execution path.
'''
def addition(a, b):
    print(a + b)

def addition(a, b, c):
    print(a + b + c)
#below call will error out as explain above
#addition(10, 20)
#this call will provide output.
addition(10, 20, 30)
    

    
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
class Supper:
    def addition(a, b):
        print(a + b)

class Chield(Super):    
    def addition(a, b, c):
        print(a + b + c)

Chield().addition(10, 20)
#addition(10, 20, 30)
    

    
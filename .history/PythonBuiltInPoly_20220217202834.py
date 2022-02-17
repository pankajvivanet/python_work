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
class Calculation:
    def addition(a, b):
        print(a + b)
        
    def addition(a, b, c):
        print(a + b + c)

c = Calculation()
c.addition(10, 20)
c.addition(10, 20, 30)
    

    
'''student=["Akash", "Harshad", "Gauri"]
college= "ABC college"

print(len(student))
print(len(college))'''


class Example:
    def __init__(self, basket):
        self.basket = list(basket)
    
    def __len__(self):
        val = len(self.basket)
        print("Value=", val)
        return val

example = Example(['Glasses','TShirt'])
print(len(example))
    
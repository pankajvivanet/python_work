

from ast import Or
from itertools import count
from math import fabs
from operator import truediv


#math_marks = int(input("Enter the mathematics marks = "))
#phy_marks = int(input("Enter the mathematics marks = "))
#chem_marks = int(input("Enter the mathematics marks = "))

#total_marks = math_marks+phy_marks+chem_marks

#average = float(total_marks/3)
'''if((average > 85.0) and (average < 100.0)):
    print("Grade A")
elif((average > 65.0) and (average < 85.0)):
    print("Grade B")
else:
    print("Grade C")
   ''' 

counter = 1
sum = 0
a = int(input("Enter the number = "))
while(counter <= 10):
    sum = sum + a
    print(a, "x", counter, "=", sum)
    counter = counter + 1

0 1
0 1 1 
0 1 1 2
0 1 1 2 3
0 1 1 2 3 5
0 1 1 2 3 5 8

'''
 true or true = true
 false or true = true
 true or false = true
 fale or false = false
 
 true and true = true
 false and true = false
 true and False= False
 false and false =False   
 '''
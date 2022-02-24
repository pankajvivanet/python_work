 #lambda
'''
 #Normal function
 def a_name(x):
     #why i'm doing this change
     x=x
     return
 #lambda function
 lambda agrguments(a...) : expretion #a + b / a*3
 '''

x = lambda a, b : a + b
#print(x(10,20))

#High-order functions python
#filter(function, itertor)
#map(function, itertor)

list_1=[1,2,3,4,5,6,7,8]
print("Filter Even numbers = ", list(filter(lambda x : x%2==0, list_1))) 

list_1=[1,2,3,4,5,6,7,8]
cubed = map(lambda x : pow(x,3), list_1)
print("Cub values=", list(cubed))


import sqlite3

conn = sqlite3.connect('text.db')
# Python code to demonstrate working of  
# lt(), le() and eq() 
  
# importing operator module  
import operator 
  
# Initializing variables 
a = 3
  
b = 3

if(operator.lt(a,b)):
    print("3 is lessthan 3")
else:
    print("3 is not lessthan 3")

if(operator.le(a,b)): 
       print ("3 is less than or equal to 3") 
else : print ("3 is not less than or equal to 3") 

if (operator.eq(a,b)): 
       print ("3 is equal to 3") 
else : print ("3 is not equal to 3") 
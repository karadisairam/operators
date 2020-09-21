import operator
li = [1, 5, 6, 7, 8]
operator.setitem(li,3,3) 
  
# printing modified list after setitem() 
print ("The modified list after setitem() is : ",end="") 
for i in range(0,len(li)): 
    print (li[i],end=" ") 
  
print ("\r") 
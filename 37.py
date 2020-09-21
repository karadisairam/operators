import operator
li=[1,5,6,7,8]

operator.delitem(li,3)
print("afret delete list :",end="")
for i in range(0,len(li)):
    print (li[i],end=" ") 

print("\r")
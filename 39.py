import operator
li=[1,5,6,7,8]
operator.delitem(li,slice(2,4))
print("modified list :",end="")
for i in range(0,len(li)):
    print(li[i],end="")

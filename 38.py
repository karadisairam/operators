import operator
li=[1,5,6,7,8]
operator.setitem(li,slice(1,4),[2,3,4])

print("after setitems of list is :",end="")
for i in range(0,len(li)):
    print(li[i],end="")


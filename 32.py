#Tuple method
a,b=10,20
print( (b,a) [a<b])

#Dictinory method
a,b=10,20
print({True:a , False:b} [a<b])

#lamba function

a,b=10,20
print((lambda: a,lambda : b) [a<b] ())
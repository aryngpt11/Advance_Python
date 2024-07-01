import copy
#a=[[1, 2], [3, 4]]
a=[1,2,3]
b=copy.deepcopy(a)
print(id(a))
print(a)

print(id(b))
print(b)

#b[1][0]=5
b[0]=5
print(id(a))
print(a)

print(id(b))
print(b)
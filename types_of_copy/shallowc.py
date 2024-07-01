#normal copy using assignment operator

""" a=['1','2','3']
print(id(a))
print(a)
b=a
print(id(b))
print(b) """

import copy
a=[[1, 2], [3, 4]]
b=copy.copy(a)
print(id(a))
print(a)

print(id(b))
print(b)

b[1][0]=5

print(id(a))
print(a)

print(id(b))
print(b)
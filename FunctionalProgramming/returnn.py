def SI(p,n,r):
    si=(p*n*r)/100
    print("Simple Interest is: ",si)
    return si
p=1000
n=9
r=9.25
s=SI  #aliases of the functions
si=s(p,n,r)
print(si)
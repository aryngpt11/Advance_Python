""" nums=[2,3,4,5,6,7,8]
numss=[]
for n in nums:
    if n%2!=0:

        c=n*n
        numss.append(c)
print(numss)

print([n*n for n in nums if n%2==0]) """ #list comphersion


""" nums=[2,3,4,5,6,7,8]
numsssq=[]
numsscube=[]
for n in nums:
    if n%2==0:

        c=n*n
        numsssq.append(c)
    
    
    else:
        c=n*n*n
        numsscube.append(c)
print(numsssq)
print(numsscube)

print([n*n  if n%2==0 else n*n*n for n in nums]) """


lst=[]
for i in range(3,6):
    for j in range(5,9):
        c=i*j
        lst.append(c)
print(lst)

#using list comphersion
print([i*j for i in range(3,6) for j in range(5,9) ])
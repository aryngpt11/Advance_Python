nums=[1,2,3,4,5]
sqq=[]
dic={}
for num in nums:
    sqq.append(num**2)
    dic[num]=num**2
print(sqq)
print(dic)

#Dict compherension

print({num:num**2 for num in nums})
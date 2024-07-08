str1="cOding"
dic={}
for char in str1:
    dic[char.upper()]= (ord(char),ord(char.swapcase()))
print(dic)


print({char.upper():(ord(char),ord(char.swapcase())) for char in str1})

#example 3 set comprehension
nums=[1,2,2,3,4]
print({n**2 for n in nums})
nums=[90,0,-34,33,-21,20]
pos=[]
neg=[]
zer=[]
other=[]
for num in nums:
    if num==0:
        zer.append("Zero is neither Positive nor Negative")
    elif num>0:
        pos.append("positive")
    elif num<0:
        neg.append("negative")
    else:
        other.append("Invalid Value ")
print(pos)
print(neg)
print(zer)


print(["positive" if num>0 else "negative" if num<0 else "Zero is neither Positive nor Negative" if num==0 else "invalid input" for num in nums])
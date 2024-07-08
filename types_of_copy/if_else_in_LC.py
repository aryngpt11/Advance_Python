num=int(input("Enter a number: "))
if num>0:
    print("Positive")
elif num==0:
    print("Zero is neither Positive nor Negative")
elif num<0:
    print("Negative")
else:
    print("Please Provide Valid Integer")

#Using List Compheresion and Chaining

print("Positive" if num>0 else "Negative" if num<0 else "Zero is neither Positive nor Negative" if num==0 else "Please Provide Valid Integer")
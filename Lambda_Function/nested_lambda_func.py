#nested lambda function

# add=lambda x:lambda y:x+y
# func=add(10)
# print(func(30))

# square=lambda n:n**2

# def modify(f):
#     num=int(input("Enter: "))
#     return f(num)+num
# print(modify(square))


square=lambda n:n**2
modify=lambda func:lambda num:func(num)+num
# var=(modify(square))
# print(var(int(input("enter the value: "))))
#or
print((modify(square)(4)))

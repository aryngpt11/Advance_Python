#nested lambda function

add=lambda x:lambda y:x+y
func=add(10)
print(func(30))
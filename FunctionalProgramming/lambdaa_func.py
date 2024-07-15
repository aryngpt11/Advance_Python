# a=lambda x,y:x+y
# print("the sum is ",a(10,20))

#sorted using lambda function


# def func(nm):
#     return nm.split()[1]
    
# data=['Sharma Rohit','Kohli Virat','Tendulkar Sachin','Raina Suresh','Gill Subham','Kishan Ishan']
# print(sorted(data,key=func))

#instead of this we can use this

    
data=['Sharma Rohit','Kohli Virat','Tendulkar Sachin','Raina Suresh','Gill Subham','Kishan Ishan']
print(sorted(data,key=lambda nm:nm.split()[1]))
#variable length positional arguments
# def summ(*nums):
#     sum1=0
#     for n in nums:
#         sum1+=n
#     print(sum1)
# summ(10,20)
# summ(5,6,7,8,9)
# summ(55,1)


#variables length keyword arguments

def summ(**nums):
    print(sum(nums.values()))
    
summ(n1=10,n2=20)
summ(n1=5,n2=6,n3=7,n4=8,n5=9)
summ(n1=55,n2=1)

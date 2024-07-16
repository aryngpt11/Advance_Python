# def even(nums):
#     for i in nums:
#         if i%2==0:
#             print(i)
#     return nums
# even([10,23,22,54,88,89])

#filter function

#we dont see the data directly while using filter() function
data=[23,22,36,54,59,90]
def even(num):
    if num%2==0:
        return True
    else:
        return False
filter_obj=filter(even,data)
print(filter_obj)
print(type(filter_obj))

for ele in filter_obj:
    print(ele)
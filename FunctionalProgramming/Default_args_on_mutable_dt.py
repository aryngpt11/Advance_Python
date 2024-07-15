def add_item(name,employee_name=[]):
    employee_name.append(name)
    print("uopdates data is: ",employee_name)

add_item("pole")
print(add_item.__defaults__)
add_item("Paul")
print(add_item.__defaults__)
add_item("pillu")
print(add_item.__defaults__)
add_item("bhat")
print(add_item.__defaults__)

print()
#To avoid this
# uopdates data is:  ['pole']
# (['pole'],)
# uopdates data is:  ['pole', 'Paul']
# (['pole', 'Paul'],)
# uopdates data is:  ['pole', 'Paul', 'pillu']
# (['pole', 'Paul', 'pillu'],)
# uopdates data is:  ['pole', 'Paul', 'pillu', 'bhat']
# (['pole', 'Paul', 'pillu', 'bhat'],)

def add_item(name,employee_name=None):
    if employee_name is None:
        employee_name=[]
    employee_name.append(name)
    print("uopdates data is: ",employee_name)

add_item("pole")

add_item("Paul")

add_item("pillu")
add_item("bhat")

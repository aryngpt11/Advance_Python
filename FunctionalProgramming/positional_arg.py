def disp(name,age):  #positional Argumanets
    print(f'Hello {name} u are {age} years old')
disp("Pillu",5)
disp(10,"pillu")

def disp(name,age):  #keyword Argumanets
    print(f'Hello {name} u are {age} years old')
disp(name="Pillu",age=5)
disp(age=10,name="pillu")
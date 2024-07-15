#Pass Function as an arguments

def get_name():
    f_nm=input("Enter ur firstname: ")
    l_nm=input("Enter ur lastname: ")
    return f_nm+" " +l_nm
def display(fun):
    print(fun())

#display(get_name()) #if i pass like this then here only return value will be save but to pass it as args we have to pass its object or we can say thata it will only call
display(get_name) #represent the full function 
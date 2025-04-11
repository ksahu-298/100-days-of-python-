#calculator
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2  
def product(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": product,
    "/": divide
}
a= float(input("Enter the 1st number : "))
b= float(input("Enter the 2nd number : "))
operation_symbol = input("Enter the operation symbol (+, -, *, /) : ")


if operation_symbol in operations:
    result_1 = operations[operation_symbol](a, b)
    print(f"{a} {operation_symbol} {b} = {result_1}")

else:
    print("Invalid operation symbol. Please use +, -, *, or /.")

again = "yes"
while again == "yes":
    again = input("Do you want to continue using the calculator? (yes/no) : ")
    if again == "yes":
        c= float(input("Enter the nextnumber : "))
        operation_symbol = input("Enter the operation symbol (+, -, *, /) : ")
        if operation_symbol in operations:
            result_2 = operations[operation_symbol](result_1, c)
            print(f"{result_1} {operation_symbol} {c} = {result_2}")
        else:
            print("Invalid operation symbol. Please use +, -, *, or /.")
    
    else :
        again == "no"
        print("Thank you for using the calculator!")
       


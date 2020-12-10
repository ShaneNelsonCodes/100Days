from Day10_Calculator_Art import logo
import os

def clear():
    os.system('cls')
   
#Add
def add(n1, n2):
    return n1 + n2
    
#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1/n2

#Operators
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for operand in operations:
        print(operand)
    calc_loop = True

    while calc_loop == True:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calc_function = operations[operation_symbol]
        answer = calc_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        calc_continue = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or type 'exit' to exit the program: ")
        if calc_continue == 'y':
            num1 = answer
        elif calc_continue == 'n':
            calc_loop = False
            calculator()
        else:
            calc_loop = False

            
calculator()


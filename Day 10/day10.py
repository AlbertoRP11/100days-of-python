# Day 10
# Functions with outputs

def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name""" #Docstring,
    if l_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formate_f_name = f_name.capitalize()
    formated_l_name = l_name.capitalize()
    return f"{formate_f_name} {formated_l_name}"

full_name = format_name("alBerto", "perUchi")
# print(full_name)

# Exercício Final
# Calculator Project

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    from art import logo

    print(logo)
    num1 = float(input("What's the first number"))
    should_continue = True
    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the lines above: ")
        num2 = float(input("What's the second number"))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "n":
            should_continue = False
            calculator()
        else:
            num1 = answer

calculator()
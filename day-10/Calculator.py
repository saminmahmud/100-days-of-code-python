# Functions with Outputs

from art import logo

def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2


def calculator():
    print(logo)
    run = True
    operations = {
        "+" : add,
        "-" : subtract,
        "*" : multiply,
        "/" : divide
    }

    num1 = float(input("What's the first number? "))

    while run:
        for symbol in operations:
            print(symbol)

        opetration_symbol = input("Type a math operation. ")

        num2 = float(input("What's the next number? "))

        function = operations[opetration_symbol]
        result = function(num1, num2)

        print(f"{num1} {opetration_symbol} {num2} = {result}")
        print(f"Type 'y' to continue calculating with {result}, type 'n' to exit or type 'new' for a brand new calculation")
        continue_calc = input("Type y/n/new: ").lower()

        if continue_calc == 'y':
          run = True
          num1 = result
        elif continue_calc == 'n':
          run = False
          print("\nGoodbye.")
        elif continue_calc == 'new':
          calculator()
        else:
          print("Invalid response.")
          run = False
          print("\nGoodbye.")

calculator()


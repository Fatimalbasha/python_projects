import calculator_art

def add(n1, n2): return n1 + n2 


def subtract(n1, n2): return n1 - n2 


def multiply(n1, n2): return n1 * n2 


def divide(n1, n2): return n1 / n2 


operations = {"+" : add, "-" : subtract, "*" : multiply, "/" : divide}

def calculator():
    should_continue = True
    print(calculator_art.logo)
    while True: 
        try: 
            num1 = float(input("What's the first number?: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number (digits only).")

    while should_continue: 
        for symbol in operations:
            print(symbol) 
        while True: 
            chossen_operation = input("Pick an operation: ")
            if chossen_operation in operations:
                break 
            else: 
                print("Invalid input. Please choose one of the operation above.")

        while True: 
            try:      
                num2 = float(input("What's the next number?: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number (digits only).")

        answer = operations[chossen_operation](num1,num2)
        print(num1, chossen_operation, num2, "=", answer)

        while True: 
            continue_calculating = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
            if continue_calculating in ["y", "n"]:
                break 
            else: 
                print("Invalid input. Please choose y or n.")

        if continue_calculating == "y":
            num1 = answer
        else:
            should_continue = False
            print('\n' * 40)
            calculator()


calculator()
    
        






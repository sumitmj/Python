#Building a simple calculator


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error, cannot divide by 0 !"
    return a / b

def calculator():
    print("Have a good time using this calculator")

    operations = [add, subtract, multiply, divide]
    operation_names = ["Addition", "Subtraction", "Multiplication", "Division"]

    while True:

        for i, name in enumerate(operation_names, start=1):
            print(f"{i}. {name}")

        try:
            user_choice =  int(input("Enter a number from 1 to 4: "))
        except ValueError:
            print("Choose a valid option")
            continue

        numb1 = int(input("Enter the first number: "))
        numb2 = int(input("Enter the second number: "))

        if 1 <= user_choice <= len(operations):
            output = operations[user_choice-1] (numb1, numb2)
            print(f"{operation_names[user_choice-1]} of {numb1} and {numb2} = {output}")
        else:
            print("Invalid option chosen")

        play_again = input("Do you want to use the calculator again? (y/n) ").lower()

        if play_again != "y":
            print("Thanks for using the calculator !")
            break
        print("\n")

if __name__ == "__main__": 
    calculator()


# This program converts Celisus ↔  Fahrenheit

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

while True:
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Quit")

    user_choice = input("Enter your choice (1/2/3): ")

    if user_choice == '1':
        temp_input = input("Enter temperature in Celsius: ")
        if temp_input.replace('.', '', 1).isdigit() or (temp_input.startswith('-') and temp_input[1:].replace('.', '', 1).isdigit()):
           celsius = float(temp_input)
           fahrenheit = celsius_to_fahrenheit(celsius)
           print(f"{celsius:.2f} °C is equal to {fahrenheit:.2f} °F")
        else:
            print("Please enter a valid number !")
    elif user_choice == '2':
        temp_input = input("Enter temperature in Fahrenheit: ")
        if temp_input.replace('.', '', 1).isdigit() or (temp_input.startswith('-') and temp_input[1:].replace('.', '', 1)):
            fahrenheit = float(temp_input)
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit:.2f} °F is equal to {celsius:.2f} °C")
        else:
            print("Please enter a valid number !")
    elif user_choice == '3':
        print("Thank for using the program !")
        break
    else:
        print("You chose invalid number. Enter a number from 1 to 3. ")








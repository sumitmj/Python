#Number System Utility Practice

import math

def fact_iterative(n):
    output = 1
    for i in range(1, n+1):
        output *= i
    return output

def fact_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * fact_iterative(n-1)

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)-1)):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b 
    return sequence

def option():
    while True:
        print("\n--- Number System Utility ---")
        print("1. Factorial (Iterative)")
        print("2. Factorial (Recursive)")
        print("3. Prime Checker")
        print("4. Fibonacci Sequence")
        print("5. Exit")

        choose = int(input("Choose an option from 1 to 5: "))

        if choose == 1:
            n = int(input("Enter a number: "))
            print(f"Factorial of {n} (Iterative) is {fact_iterative(n)}")
        elif choose == 2:
            n = int(input("Enter a number: "))
            print(f"Factorial of {n} (Recursive) is {fact_recursive(n)}")
        elif choose == 3:
            n = int(input("Enter a number: "))
            print(f"{n} is a prime number.")
        elif choose == 4:
            n = int(input("Enter a number: "))
            print(f"Fibonacci sequence ({n} terms): {fibonacci(n)}")
        elif choose == 5:
            print("Thank you for using this program")
            break
        else:
            print("Input a valid number !")

option()
            
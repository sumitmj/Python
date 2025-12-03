sum_of_odd = 0
sum_of_even = 0 

while True:
    user_input = input("Enter any number and Press Enter to quit. ")
    if user_input == "":
        break
    user_input = int(user_input)
    if user_input % 2 == 0:
        sum_of_even += user_input
    else:
        sum_of_odd += user_input
    
print("Sum of Even Number is ", sum_of_even)
print("Sum of Odd Number is ", sum_of_odd)

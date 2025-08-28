#Program to print my full name or first name or last name
#Depends upon the input provided

for i in range(1,51):
    if i % 2 == 0 and i % 3 == 0:
        print("Sumit Maharjan")
    elif i % 2 == 0:
        print("Sumit")
    elif i % 3 == 0:
        print("Maharjan")
    else:
        print(i)
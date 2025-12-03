user_sentence = input("Enter a sentence: ")

letters = 0
digits = 0

for char in user_sentence:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1

print("Number of letters is ", letters)
print("Number of digits is ", digits)
#write a program to enter a 10 digit number and check if it is valid or not
number = input("Enter a 10 digit number: ")
if len(number) == 10 and number.isdigit():
    print("The number is valid.")
else:
    print("The number is not valid.")
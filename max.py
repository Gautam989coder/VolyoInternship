#write a program to find the maximum of three numbers

from unittest import case


a = float(input("Enter first number: "))
b= float(input("Enter second number: "))    
c = float(input("Enter third number: "))
if (a >= b) and (a >= c):
   print("The largest number is ", a)
elif (b >=a) and (b >= c):
   print("The largest number is", b)
else:
    print("The largest number is", c)



#--------------------------------------------------------
#Write a program to switch case of number
day = int(input("Enter a number (1-7): "))
match day:  
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:     
        print("Invalid input! Please enter a number between 1 and 7.")
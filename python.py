#Write a program to find the number is even or odd.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.") 



#--------------------------------------------------------------
#Write a program to find Leap Year or not.
year = int(input("Enter a year: "))     
if year % 4 == 0 :
    print(year, "is a leap year.")
elif year % 100 == 0:
    print(year, "is not a leap year.")      
elif year % 400 == 0:
    print(year, "is a leap year.")  
else:    
    print(year, "is not a leap year.")
    

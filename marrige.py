gen=input("Enter Your Gender: ")
if gen=="male":
    age=int(input("Enter your age: "))
    if age>=21:
        print("congratulations! You are Eligible for marriage")
    else:
        print("sorry! You are not Eligible for marriage ")
elif gen=="female":
    age=int(input("Enter your age: "))
    if age>=18:
        print("congratulations! You are Eligible for marriage")
    else:
        print("sorry! You are not Eligible for marriage")
elif gen=="other":
    print("Sorry! we have don't have any information about other")
else:
    print("Invalid input! Please enter a valid gender")
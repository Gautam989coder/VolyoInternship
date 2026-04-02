minutes=int(input("Enter the minutes: "))

min1 = 3
min2_10 = 2
min11 = 1

cost = 0
if minutes == 1:
    cost = min1
elif minutes >= 2 and minutes <= 10:
    cost = min1 + (minutes - 1) * min2_10
else:
    cost = min1 + (9 * min2_10) + (minutes - 10) * min11

print("The cost of the call is:",cost, "cents")
dogYear=int(input("Enter dog's age converted to human year: "))
if  dogYear==1:
    print("dog age is 15 according to human year")
elif dogYear==2:
    print("dog age is 24 according to human year")
else:
    humanYear=24+(dogYear-2)*4
    print("dog age is", humanYear, "according to human year")    


#write a program to cat age converted to human year  
cat=float(input("Enter cat's age converted to human year: ")) 
def catAge(cat):
    if cat==1:
        return 12.5
    elif cat==2:
        return 12.5*2
    else:
        return 12.5*2+(cat-2)*4

print("cat age is", catAge(cat), "according to human year")  
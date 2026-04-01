#write a program to enter a year and find the century of that year

year=int(input("Enter a year: "))
def solution(year):
    if year%100==0:
        return year//100
    else:     
        return year//100 + 1
    
print(solution(year))

saal= int(input("Enter a year: "))
def century(saal):
    return (saal + 99) // 100
print(century(saal))
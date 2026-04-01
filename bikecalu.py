bike=int(input("Enter the length:"))
def bikecalu(bike):
    hour=bike//60%24
    minute=bike%60
    return hour, minute
hour, minute= bikecalu(bike)
print(f"{hour:02d}:{minute:02d}")

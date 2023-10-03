import calendar
year:int = int(input("What is the year? "))

print(f"The year {'is' if calendar.isleap(year) else 'is not'} a leap year")
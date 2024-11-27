#Check the leap year

year = int (input ('Enter any year that is to be checked for leap year: '))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Given year is a leap year")
else:
    print("It's not a leap year")
    
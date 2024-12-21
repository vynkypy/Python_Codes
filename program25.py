#  User will input (3ages).Find the oldest one

first_age = int(input("Enter first age: "))
second_age = int(input("Enter second age: "))
third_age = int(input("Enter third age: "))

if first_age > second_age and first_age > third_age:
    print(f"{first_age} is oldest")

elif second_age > first_age and second_age > third_age:
    print(f"{second_age} is oldest")

else:
    print(f"{third_age} is oldest")



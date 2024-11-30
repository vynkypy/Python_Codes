# Find the largest of three numbers

# Input three numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

# Compare the numbers to find the largest
if a >= b and a >= c:
    print(f"Largest number is {a}")
elif b >= a and b >= c:
    print(f"Largest number is {b}")
else:
    print(f"Largest number is {c}")

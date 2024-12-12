# Find the givene number is perfect or not

def is_perfect_number(num):
    sum_of_divisors = 0
    for i in range(1, num):  # Check numbers less than num
        if num % i == 0:    # If it's a divisor
            sum_of_divisors += i
    return sum_of_divisors == num

# Input from the user
number = int(input("Enter a number: "))
if is_perfect_number(number):
    print(f"{number} is a Perfect Number!")
else:
    print(f"{number} is NOT a Perfect Number.")

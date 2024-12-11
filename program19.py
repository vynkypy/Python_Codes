# check weather given number is prime or not

def is_prime(number):
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, number):  # Check divisibility from 2 up to the number-1
        if number % i == 0:
            return False  # If divisible by any number other than 1 and itself, it's not prime
    return True

# Take input directly and check if it's prime
try:
    number = int(input("Enter a number to check if it is prime: "))
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is NOT a prime number.")
except ValueError:
    print("Please enter a valid integer.")

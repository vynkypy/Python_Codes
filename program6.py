# Python Program to check given number is an Armstrong number or not.

# Input : 153
# Output : Yes
# 153 is an Armstrong number.
# 1*1*1 + 5*5*5 + 3*3*3 = 153

print("Please enter the int number!!")

num = int(input("Enter a number: "))

print(type(num))

num_str = str(num)
num_length = len(num_str)
sum_of_powers = 0

for digit in num_str:
    temp_value = int(digit) ** num_length
    sum_of_powers = temp_value + sum_of_powers
print(sum_of_powers)
if sum_of_powers == num:
    print("Given number is an Amstrong number!")
else:
    print("Given number is not an Amstrong number!")
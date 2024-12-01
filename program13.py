# Find the sum of all even numbers from 1 to a given number

n = int(input("Enter a number: "))

even_sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:  
        even_sum += i 

print(f"The sum of all even numbers from 1 to {n} is {even_sum}")

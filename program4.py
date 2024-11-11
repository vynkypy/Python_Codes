# substraction of given numbers

a = int(input('Enter how many numbers you want substraction of: '))

ans = 0

for i in range(a):
    b = int(input(f'Enter number {i}: '))
    ans = b - ans

print('Substraction of given numbers is: ', ans)
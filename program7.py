# Python code for simple calculator

(print("1 For Addition "))
(print("2 For Substraction "))
(print("3 For Multiplication "))
(print("4 For Division "))

operation = int(input("Enter your preferance: "))

if operation == 1:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    ans = a + b

    print("Addiion of given numbers is : ", ans)

elif operation == 2:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    ans = a - b

    print("Substraction of given numbers is : ", ans)

elif operation == 3:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    ans = a * b

    print("Multiplication of given numbers is : ", ans)

elif operation == 4:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    ans = a // b

    print("Division of given numbers is : ", ans)

else:
    print("Wrong input")

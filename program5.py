# Python Program for Simple Interest

# Simple interest formula is given by: 
# Simple Interest = (P x T x R)/100 Where, P is the principal amount T is the time and R is the rate

principal = int(input("what is the principle ampount: "))
time = int(input("What should be the time period (in Years): "))
rate = float(input("What should be the rate of interest: "))

si = (principal * time * rate)/100

print("The simple interest for your amount is: ", si)
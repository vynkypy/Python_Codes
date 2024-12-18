n = 18

if n%2 != 0:
    print("Weird")

elif n%2 == 0:
    for i in range(2,5):
        if i == n:
            print("Not Weird")
    
    for j in range(6,20):
        if j == n:
            print("Weird")
    
    for k in range(20, 100):
        if n > k:
            print("Not Weird")
            break


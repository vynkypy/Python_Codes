# Find the smallest element in the list

ls = [5, 6, 3, 4, 7, 3, 8, 9, 10, 21, 23, 24, 25]

temp = ls[0]

for i in range(1, len(ls)):
    if temp > ls[i]:
        temp = ls[i]

print(temp)

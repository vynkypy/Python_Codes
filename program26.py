#sort a list without using sort keyword

num_list = [41,2,42,78,84,22,34,54,31,45,2,4,5,6,9]

sorted_list = []
temp = num_list[0]

for i in range(len(num_list)):
    for j in range(i+1, len(num_list)):
        if num_list[i] > num_list[j]:
            num_list[i], num_list[j] = num_list[j], num_list[i]

print(num_list)



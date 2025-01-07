# Find the Frequency of Each Element in a List

# Input: [1, 2, 2, 3, 4, 4, 4]
# Output: {1: 1, 2: 2, 3: 1, 4: 3}

# input_list = [1, 2, 2, 3, 4, 4, 4]

# length = len(input_list)

# output_dict = {}

# for i in range(length):
#     count = 0
#     for j in range(length):
#         if input_list[i] == input_list[j]:
#             count += 1
#     output_dict[input_list[i]] = count

# # To remove duplicate keys, you can convert the dictionary to a final version with unique keys
# final_output = {}
# for key, value in output_dict.items():
#     final_output[key] = value

# print(final_output)


input_list = [1, 2, 2, 2, 3, 4, 4, 4, 3]
print(input_list)
length = len(input_list)

output_dict = {}
count = 0

for i in range(length):
    count = 0
    for j in range(length):
        if input_list[i] == input_list[j]:
            count += 1
    output_dict[input_list[i]] = count
print(output_dict)

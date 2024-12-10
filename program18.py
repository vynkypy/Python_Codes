# hollow squre pattern

size = 5

for i in range(size):
    if i == 0 or i == size - 1:
        print('* ' * size)  # Print full row for top and bottom
    else:
        print('* ' + '  ' * (size - 2) + '*')  # Print hollow rows with border

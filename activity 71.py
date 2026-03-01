count = 0
array1 = ('i', [1, 3, 5, 3, 7, 9, 3])
for i in array1:
    if i == 3:
        count += 1
print("Number of occurrences of 3: ", count)
print("Reversed list: ", array1[1][::-1])

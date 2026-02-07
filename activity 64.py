list = []
count = 0
for i in range(1, 11):
    list.append(i)
    count += i
avg = count / len(list)
print("Average: ", avg, "Highest: ", max(list), "Smallest: ", min(list))
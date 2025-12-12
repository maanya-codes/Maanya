trees = []
for count in range(6):
    trees.append(int(input(f"Enter the amount of trees in Area {count + 1}: "))) 
print("The average number of trees in all 6 areas are:", sum(trees)/len(trees))
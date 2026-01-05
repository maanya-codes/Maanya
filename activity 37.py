size = int(input("How many rows in the triangle?: "))
x = 0
for i in range(size):
    for j in range(i+1):
        print("*", end=" ")
    print()
    
    

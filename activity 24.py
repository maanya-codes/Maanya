s1 = int(input("Enter speed for Cyclist 1: "))
s2 = int(input("Enter speed for Cyclist 2: "))
s3 = int(input("Enter speed for Cyclist 3: "))
avg = (s1 + s2 + s3)/3
speeds = [s1, s2, s3]
count = 0
for i in speeds:
    count += 1
    if i > avg:
        print(f"Cyclist {count} is above average speed by {i - avg}")
    elif i < avg:
        print(f"Cyclist {count} is below average speed by {avg - i}")
    else: 
        print(f"Cyclist {count} is exactly average speed")

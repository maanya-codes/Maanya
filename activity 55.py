valid = False
while not valid:
    try:
        x = int(input("Enter an integer:"))
        while x%2==0:
            print("bye")
        valid = True
    except ValueError:
        print("Error occurred.")
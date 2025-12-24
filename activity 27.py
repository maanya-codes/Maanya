print("Choose your ride!\nEnter 1 for a bike  |  Enter 2 for a car")
choice = int(input("Enter your input: "))

if choice == 1:
    print("Wow you are feeling adventurous!")
    print("Enter 1 for a classic model  |  Enter 2 for a sports model")
    choice1 = int(input("Enter your input: "))
    if choice1 == 1:
        print("You have chosen a classic bike")
    else:
        print("You have chosen a sports bike")
elif choice == 2:
    print("You are boring cause you chose a car")
    print("Enter 1 for a classic model  |  Enter 2 for a sports model")
    choice2 = int(input("Enter your input: "))
    if choice2 == 1:
        print("You have chosen a classic car")
    else:
        print("You have chosen a sports car")
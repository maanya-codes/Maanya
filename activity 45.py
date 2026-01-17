print("Welcome to the awesome season predictor!")

def predict():
    userInput = input("Is it very hot? (Enter YES/NO)")
    if userInput == "YES":
        print("You're having summer right now")
    elif userInput == "NO":
        userInput = input("Are all the plants blooming around you? (Enter YES/NO)")
        if userInput == "YES":
            print("You're having spring right now")
        elif userInput == "NO":
            userInput = input("Are the trees' leavers red/orange? (Enter YES/NO)")
            if userInput == "YES":
                print("You're having autumn right now")
            elif userInput == "NO":
                userInput = input("Is it really cold and snowing? (Enter YES/NO)")
                if userInput == "YES":
                    print("You're having winter right now")
                elif userInput == "NO":
                    print("IDK")

predict()
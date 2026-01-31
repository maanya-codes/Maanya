import random
playing = True
while playing:
    print("=== Welcome to the Number Guessing Game! ===")
    num = random.randint(1, 101)
    print("In this game, you have to guess what number I am thinking of from 1 to 100!")
    guess = int(input("Enter your guess: "))
    while guess != num:
        if guess > num:
            print("The answer is lower :(")
            guess = int(input("Enter your guess: "))
        elif guess < num:
            print("The answer is higher :(")
            guess = int(input("Enter your guess: "))
    print("Yay! Your answer is right!")
    play = input("Would you like to continue playing? (Y/N) : ")
    if play == "Y":
        playing = True
    elif play == "N":
        print("Exiting game..")
        playing = False

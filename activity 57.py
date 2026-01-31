import random
#rock, paper, scissor
while True:
    possibleActions = ["rock", "paper", "scissors"]
    userAct = input("Enter a choice [rock, paper, scissors] : ")
    compAct = random.choice(possibleActions)
    if userAct == compAct:
        print(f"Both players selected {userAct}. It's a tie!")
    elif userAct == "rock":
        if compAct == "scissors":
            print("You chose rock and computer chose scissors.\n You win.")
        else:
            print("You chose rock and computer chose paper.\n You lose.")
    elif userAct == "paper":
        if compAct == "rock":
            print("You chose paper and computer chose rock.\n You win.")
        else:
            print("You chose paper and computer chose scissors.\n You lose.")
    elif userAct == "scissors":
        if compAct == "paper":
            print("You chose scissors and computer chose paper.\n You win.")
        else:
            print("You chose scissors and computer chose rock.\n You lose.")
    


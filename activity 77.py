import random

board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def display():

    print(board[0], " | ",board[1], " | ",board[2], " | ")

    print("---+-----+------")

    print(board[3], " | ",board[4], " | ",board[5], " | ")

    print("---+-----+------")

    print(board[6], " | ",board[7], " | ",board[8], " | ")

def player_play():

    pos = int(input("Where do you want to put your X?: "))
    while board[pos-1] in ["X", "O"]:
        pos = int(input("Already Taken. Where do you want to put your X?: "))
    board[pos-1] = "X"

def comp_play():
    pos = random.randint(0, 8)
    while board[pos] in ["X", "O"]:
       pos = random.randint(0, 8) 
    board[pos] = "O"
   

   

def win():

    if board[0] == board [1] and board[1] == board [2] and board[2] == "X":

        win = "Y"

        winner = "Player"

        return  win, winner
    elif board[3] == board [4] and board[4] == board [5] and board[5] == "X":

        win = "Y"

        winner = "Player"

        return win, winner

    elif board[6] == board [7] and board[7] == board [8] and board[8] == "X":

        win = "Y"

        winner = "Player"

        return win, winner

    elif board[0] == board [3] and board[3] == board [6] and board[6] == "X":

        win = "Y"

        winner = "Player"

        return win, winner

    elif board[1] == board [4] and board[4] == board [7] and board[7] == "X":

        win = "Y"

        winner = "Player"

        return win, winner

    elif board[2] == board [5] and board[5] == board [8] and board[8] == "X":

        win = "Y"

        winner = "Player"

        return win, winner

    elif board[0] == board [4] and board[4] == board [8] and board[8] == "X":

        win = "Y"

        winner = "Player"

        return win, winner

    elif board[2] == board [4] and board[4] == board [6] and board[6] == "X":

        win = "Y"

        winner = "Player"

        return win, winner

    #---------------------------------------------------

    elif board[0] == board [1] and board[1] == board [2] and board[2] == "O":

        win = "Y"

        winner = "Computer"

        return win, winner

    elif board[3] == board [4] and board[4] == board [5] and board[5] == "O":

        win = "Y"

        winner = "Computer"

        return win, winner

    elif board[6] == board [7] and board[7] == board [8] and board[8] == "O":

        win = "Y"

        winner = "Computer"

        return win, winner

    elif board[0] == board [3] and board[3] == board [6] and board[6] == "O":

        win = "Y"

        winner = "Computer"

        return win, winner

    elif board[1] == board [4] and board[4] == board [7] and board[7] == "O":

        win = "Y"

        winner = "Computer"

    elif board[2] == board [5] and board[5] == board [8] and board[8] == "O":

        win = "Y"

        winner = "Computer"

        return win, winner

    elif board[0] == board [4] and board[4] == board [8] and board[8] == "O":

        win = "Y"

        winner = "Computer"

        return win, winner

    elif board[2] == board [4] and board[4] == board [6] and board[6] == "O":

        win = "Y"

        winner = "Computer"

        return win, winner

    else:
        win = "N"
        winner = "NULL"
        return win, winner



def main():

    print("Let's play TIC TAC TOE!")

    while True:

        display()

        player_play()

        comp_play()

        display()

        is_win, winner = win()

        if is_win == "Y":
            print(winner, "is the winner!")
            break
        elif win == "N":
            continue
        if not any(spot.isdigit() for spot in board):
            print("ITS A DRAW")
            break


       

main()

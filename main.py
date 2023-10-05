# Setup variables

import random
player1 = " "
player2 = " "
turn = 0
replay = 1
chosensquare = 10
win = 0
range_1 = range(1, 9)
win
p2win = 0
p1win = 0

# Choosing usernames

player1 = input("Please choose a name for player 1 ")
player2 = input("Please choose a name for player 2 ")

# Deciding turns

while replay == 1:

    print(player1 + " has won " + str(p1win) + " times.")
    print(player2 + " has won " + str(p2win) + " times.")

    win = 0

    # Board is stored as a list, as I have no idea how else to do it.

    board = [" "," "," "," "," "," "," "," "," "]

    turn = random.randrange(1, 3)

    print("First turn goes to player " + str(turn) + ".")

    while win == 0:
        chosensquare = 10
        print("|" + board[0] + "|" + board[1] + "|" + board[2] + "|")
        print("-------")
        print("|" + board[3] + "|" + board[4] + "|" + board[5] + "|")
        print("-------")
        print("|" + board[6] + "|" + board[7]+"|" + board[8] + "|")
        if turn == 1:
            while int(chosensquare) not in range_1:
                chosensquare = input("Please choose a square between 1 and 9 ")
                if int(chosensquare) not in range_1 or board[int(chosensquare)-1] != " ":
                    print("Please choose a valid number")
                    print(int(chosensquare) -1)
                else:
                    print("You have chosen square " + chosensquare + ".")
                    board[int(chosensquare) - 1] = "O"
                    turn = 2
        if turn == 2:
            while int(chosensquare) not in range_1:
                chosensquare = input("Please choose a square between 1 and 9 ")
                if int(chosensquare) not in range_1 or board[int(chosensquare)-1] != " ":
                    print("Please choose a valid number")
                else:
                    print("You have chosen square " + chosensquare + ".")
                    board[int(chosensquare)-1] = "X"
                    turn = 1

        if board[0] == "O":
            if board[1] == "O":
                if board[2] == "O":
                    print(player1 + " wins!")
                    win = 1
                    p1win = p1win + 1
            elif board[3] == "O":
                if board[6] == "O":
                    print(player1 + " wins!")
                    win = 1
                    p1win = p1win + 1
            elif board[4] == "O":
                if board[8] == "O":
                    print(player1 + " wins!")
                    win = 1
                    p1win = p1win + 1
        elif board[1] == "O":
            if board[4] == "O":
                if board[7] == "O":
                    print(player1 + " wins!")
                    win = 1
                    p1win = p1win + 1
        elif board[2] == "O":
            if board[5] == "O":
                if board[8] == "O":
                    print(player1 + " wins!")
                    win = 1
                    p1win = p1win + 1
            elif board[4] == "O":
                if board[6] == "O":
                    print(player1 + " wins!")
                    win = 1
                    p1win = p1win + 1
        elif board[3] == "O":
            if board[4] ==  "O":
                if board[5] == "O":
                    print(player1 + " wins!")
                    win = 1
                    p1win = p1win + 1
        elif board[6] == "O":
            if board[7] == "O":
                if board[8] == "O":
                    print(player1 + " wins!")
                    win = 1
                    p1win = p1win + 1

        if board[0] == "X":
            if board[1] == "X":
                if board[2] == "X":
                    print(player2 + " wins!")
                    win = 1
                    p2win = p2win + 1
            elif board[3] == "X":
                if board[6] == "X":
                    print(player2 + " wins!")
                    win = 1
                    p2win = p2win + 1
            elif board[4] == "X":
                if board[8] == "X":
                    print(player2 + " wins!")
                    win = 1
                    p2win = p2win + 1
        elif board[1] == "X":
            if board[4] == "X":
                if board[7] == "X":
                    print(player2 + " wins!")
                    win = 1
                    p2win = p2win + 1
        elif board[2] == "X":
            if board[5] == "X":
                if board[8] == "X":
                    print(player2 + " wins!")
                    win = 1
                    p2win = p2win + 1
            elif board[4] == "X":
                if board[6] == "X":
                    print(player2 + " wins!")
                    win = 1
                    p2win = p2win + 1
        elif board[3] == "X":
            if board[4] ==  "X":
                if board[5] == "X":
                    print(player2 + " wins!")
                    win = 1
                    p2win = p2win + 1
        elif board[6] == "X":
            if board[7] == "X":
                if board[8] == "X":
                    print(player2 + " wins!")
                    win = 1
                    p2win = p2win + 1
    print("Would you like to play again?")
    win = input("Please type 0 to play again or 1 to finish ")
    if win == 1:
        print("Thanks for playing")
        print(player1 + " has won " + p1win + " times")
        print(player2 + " has won" + p2win + " times")
        if p1win > p2win:
            print(player1 + " wins!")
        elif p2win > p1win:
            print(player2 + " wins!")
        else:
            print(player1 + " and " + player2 + " drew!")
        exit()












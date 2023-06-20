board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
win = False
turn = 1

def player_turn(player):
    global turn

    print(f"Choose {player}'s move.")
    row = int(input("What row do you want to select? 1, 2, or 3? "))-1
    column = input("What column do you want to select? A, B, or C? ")

    if column == "A" or column == "a":
        column = 0
    elif column == "B" or column == "b":
        column = 1
    else:
        column = 2
        
    if board[row][column] == "-":
        board[row][column] = player
        turn = turn+1
    else:
        print("\nSorry, that space is not available!")

def wincheck():
    print("\nCurrently the board stands as follows:")
    for i in board:
        print(*i)

    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
        print("X wins with the top row")
        return True
    elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
        print("X wins with the middle row")
        return True
    elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
        print("X wins with the bottom row")
        return True
    elif board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
        print("O wins with the top row")
        return True
    elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
        print("O wins with the middle row")
        return True
    elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
        print("O wins with the bottom row")
        return True
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        print("X wins with the first column")
        return True
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        print("X wins with the middle column")
        return True
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        print("X wins with the last column")
        return True
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
        print("O wins with the first column")
        return True
    elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
        print("O wins with the middle column")
        return True
    elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
        print("O wins with the last column")
        return True
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        print("X wins with a descending diagonal")
        return True
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        print("X wins with an ascending diagonal")
        return True
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        print("O wins with a descending diagonal")
        return True
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        print("O wins with an ascending diagonal")
        return True
    else:
        return False

print("We're playing tic-tac-toe!")

while win == False and turn <10:
    if turn %2 == 0:
        player_turn("O")
    else:
        player_turn("X")

    win = wincheck()

if turn == 10:
    print("Cat's game, nobody wins")
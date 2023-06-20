board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
win = False
turn = 1

def player_turn(player):
    """
    Requests and validates player row and column input.

    Parameters
    ----------
    player: string
        "X" or "O"
    
    Returns
    -------
    board: list
        Updated player board with moves recorded as a nested list
    turn: integer
        Counts the number of turns to regulate gameplay
    """
    
    global turn
    row = 9
    column = 9

    while (row == 9 and column == 9) or (board[row][column] != "-"):
        print(f"Choose {player}'s move:")
        row = input("What row do you want to select? 1, 2, or 3? ")
        while row not in ["1", "2", "3"]:
            print("That's not an option!")
            row = input("What row do you want to select? 1, 2, or 3? ")

        row = int(row) - 1

        column = input("What column do you want to select? A, B, or C? ").lower()
        while column not in ["a", "b", "c"]:
            print("That's not an option!")
            column = input("What column do you want to select? A, B, or C? ").lower()
        
        if column == "a":
            column = 0
        elif column == "b":
            column = 1
        elif column == "c":
            column = 2

        if board[row][column] != "-":
            print("Sorry, that space is taken!")
    
    board[row][column] = player
    turn = turn + 1

    return board, turn

def wincheck():
    """
    Prints the board as it currently stands in a readable format and checks for win conditions. 

    Returns
    -------
    boolean
        If win conditions met (aka someone has won), True returned
    """

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
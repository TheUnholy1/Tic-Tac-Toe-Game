import random

board = [' ' for i in range(9)]
exit_Condition = False
game_Winner = None
game_Running = True
current_Player = 'X'

def printBoard():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def player_Input():
    try:
        turn = int(input("Please Enter a number from 1 - 9, or 0 to Exit: "))
    except ValueError:
        print("Invalid Input.Please try Again!")
        return False
    if turn == 0:
        return True
    if turn >= 1 and turn <= 9 and board[turn - 1] == " ":
        board[turn-1] = current_Player
        check_Winner()
        switchPlayer()

    else:
        print('Invalid Turn! Try Again')


def switchPlayer():
    global  current_Player
    if current_Player == 'X':
        current_Player = 'O'
        computer_Move()
        current_Player = 'X'
    else:
        current_Player = 'X'

def check_Winner():
    winning_Combination = [[0,1,2],[3,4,5], [6,7,8], #row
                           [0,3,6], [1,4,7], [2,5,8], # column
                           [0,4,8], [6,4,2] # diagonal
                           ]
    for a,b,c in winning_Combination:
        global game_Winner
        if board[a] == board[b] == board[c] and board[a] != ' ':
            game_Winner = board[a]
            return True

def computer_Move():
    while True:
        attack = random.randint(1,9)
        if board[attack-1] == ' ':
            board[attack-1] = 'O'
            return False



def main():
    while game_Running:
        global  exit_Condition
        printBoard()
        exit_Condition = player_Input()
        if exit_Condition:
            print("Game Over. Exiting the Game...")
            break
        if check_Winner():
            printBoard()
            print(f"Player {game_Winner} wins!")
            break
        if " " not in board:
            print("Its a tie!")
            printBoard()
            break


if __name__ == "__main__":
    main()

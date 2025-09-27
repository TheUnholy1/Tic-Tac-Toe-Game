import os
player = 'X'
winner = None

def clear_console():
    """Clears the console screen."""
    # Check the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

board = [' ' for x in range(9)]

def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    

def check_win():
    global winner
    if board[0] == board[1] == board[2] and board[0] != ' ':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != ' ':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != ' ':
        winner = board[6]
        return True
    elif board[0] == board[3] == board[6] and board[0] != ' ':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != ' ':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != ' ':
        winner = board[2]
        return True
    elif board[0] == board[4] == board[8] and board[0] != ' ':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != ' ':
        winner = board[2]
        return True 
    else:
        return False



while True:
    # clear_console()
    print_board()
    attack = int(input("Enter your move (1-9): "))
    if attack == 0:
        print("Game exited.")
        break
    if attack >=1 and attack <=9 and board[attack-1] == ' ':
        board[attack-1] = player
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
    else:
        clear_console()
        print("Invalid move. Try again.")
    if check_win():
        clear_console()
        print(f"Player {winner} wins!")
        print_board()
        break
    if ' ' not in board:
        clear_console()
        print("It's a tie!")
        print_board()
        break
    
print("Game over.")

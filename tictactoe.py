"""This is a simple Tic Tac Toe game where a player plays against the computer."""
import os
import random

CURRENT_PLAYER = 'X'
GAME_WINNER = None
GAME_RUNNING = True
board = [' ' for x in range(9)]

def clear_console():
    """Clears the console screen."""
    # Check the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

def print_board():
    """Function printing the game board"""
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    

def check_win():
    """This is a function to check if there is a winner."""
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

def computer_move():
    """Function for the computer to make a move."""
    while CURRENT_PLAYER == 'O':
        position = random.randint(0, 8)
        if board[position] == ' ':
            board[position] = 'O'
        switch_player()
        break

def switch_player():
    """Function to switch the current player."""
    global CURRENT_PLAYER
    if CURRENT_PLAYER == 'X':
        CURRENT_PLAYER = 'O'
    else:
        CURRENT_PLAYER = 'X'   
def player_input():
    """Function to take player input"""
    global GAME_RUNNING
    global CURRENT_PLAYER
    attack = int(input("Enter your move (1-9): "))
    if attack == 0:
        return True
    if attack >=1 and attack <=9 and board[attack-1] == ' ':
        board[attack-1] = CURRENT_PLAYER
        if CURRENT_PLAYER == 'X':
            CURRENT_PLAYER = 'O'
            computer_move()
        else:
            CURRENT_PLAYER = 'X'
    else:
        print("Invalid move. Try again.")
while GAME_RUNNING:
    print_board()
    EXIT_CONDITION = player_input()
    if EXIT_CONDITION:
        print('Game Over. Exiting...')
        GAME_RUNNING = False
    if check_win():
        clear_console()
        print(f"Player {CURRENT_PLAYER} wins!")
        print_board()
        GAME_RUNNING = False
    if ' ' not in board:
        clear_console()
        print("It's a tie!")
        print_board()
        GAME_RUNNING = False

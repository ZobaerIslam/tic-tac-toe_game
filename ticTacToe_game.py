#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 04:01:21 2020

@author: Zobaer Islam
"""

# Import OS for Clear Output
import os

# Global variables
board = [' '] * 10
game_state = True
annouce = ''

# Game will ignore the 0 index
def reset_board():
    global board, game_state
    board = [' '] * 10
    game_state = True
    
def display_board():
    # Clear_output()
    os.system('clear' if os.name == 'posix' else 'cls')
    
    # Print board
    print (" " + board[7] + " | " + board[8] + " | " + board[9] + " ")
    print ("-----------")
    print (" " + board[4] + " | " + board[5] + " | " + board[6] + " ")
    print ("-----------")
    print (" " + board[1] + " | " + board[2] + " | " + board[3] + " ")
    
def win_check(board, player):
    ''' Check Horizontal, Verticals and Diagonals for a win.'''
    if ((board[7] == board[8] == board[9] == player) or
    (board[4] == board[5] == board[6] == player) or
    (board[1] == board[2] == board[3] == player) or
    (board[7] == board[4] == board[1] == player) or
    (board[8] == board[5] == board[2] == player) or
    (board[9] == board[6] == board[3] == player) or
    (board[7] == board[5] == board[3] == player) or
    (board[9] == board[5] == board[1] == player)):
        return True
    else:
        return False
    
def full_board_check(board):
    '''Function to check if any remaining blanks are in the board'''
    if " " in board[1:]:
        return False
    else:
        return True
    
def ask_player(mark):
    '''Ask player where to place X or O mark, check validity'''
    global board
    req = 'Choose where to place your: ' + mark + ' '
    while True:
        try:
            choice = int(input(req))
        except (ValueError):
            print('Sorry, Please input a number between 1-9.')
            continue
        
        if choice <= 0 or choice >= 10 :
            print('Sorry, Please input a number between 1-9.')
            continue
        
        if board[choice] == " ":
            board[choice] = mark
            break
        else:
            print("Sorry, That space isn't empty!")
            continue
        
def player_choice(mark):
    global board, game_state, announce
    
    # Set game blank game announcement
    announce = ''
    
    # get player input
    mark = str(mark)
    
    # Validate input
    ask_player(mark)
    
    # Clear_output()    
    os.system('clear' if os.name == 'posix' else 'cls')
    
    # Check for player Win
    if win_check(board, mark):
        
        # Display board
        display_board()
        announce = mark + " Wins! Congratulation."
        game_state = False
    
    # Show board
    display_board()
    
    # Check for a tie
    if full_board_check(board):
        announce = 'Opos! Tie.'
        game_state = False
    
    return game_state, announce

def play_game():
    reset_board()
    global announce, game_state
    
    # Set Marks
    X = 'X'
    O = 'O'
    
    while True: 
        # Clear_output()
        os.system('clear' if os.name == 'posix' else 'cls')
        
        # Show board
        display_board()
        
        # Player X turn
        game_state, announce = player_choice(X)
        print(announce)
        if game_state == False:
            break
        
        # Player O turn
        game_state, announce = player_choice(O)
        print(announce)
        if game_state == False:
            break
        
    rematch = input("Would you like to play again? y/n: ")
    if rematch == 'y':
        play_game()
    else:
        print("Thanks for playing!")
        
play_game()


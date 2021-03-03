# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 12:32:03 2021

@author: eynavptia
""" 
import random
import os


# Function to display the Tic Tac Toe board status
def display(board):
    print(board)

# Fucntion to clear the output each turn
def clear():
   os.system('cls')

#Randon the first to play
def choose_first():
    first = random.randint(1,2)
    if first == 1:
        player1 = marker();
        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'
    else:
        player2 = marker();
        if player2 == 'X':
            player1 = 'O'
        else:
            player1 = 'X'
    return player1,player2

# Function to set the first player his marker
def marker():
    choice = input('player 1 please choose "X" or "O" :')
    while choice!='X' and  choice!='O':
        choice = input('player 1 please choose "X" or "O": ')
    return choice

# Function to get the player position he wants
def player_position():
    choice = 'START'
    while choice.isdigit() == False:
        choice = input('please enter the position you want: ')
        if choice.isdigit() == False:
            print('Please enter an integer number')
        elif int(choice)<1 or int(choice)>9:
            print('Please enter a number between 1 to 9')
            choice = 'AGAIN'
    choice = int(choice)
    return choice

#  Setting the player position he chose on the board       
def set_position_player(player,board):
    position = player_position()
    while board[position-1]!= '':
        print('Please choose a differnt position')
        position = player_input()
    if player == 'X':
        board[position-1]='X'
    else:
        board[position-1]='O'
    return board

# checking if the game can countiue of the game as ended
def board_checking(player1,player2,board):
    
    #Checking if the player 1 won
    if board[0]==player1 and board[3]==player1 and board[6]==player1:
        return 1
    elif board[0]==player1 and board[1]==player1 and board[2]==player1:
        return 1
    elif board[2]==player1 and board[5]==player1 and board[8]==player1:
        return 1
    elif board[6]==player1 and board[7]==player1 and board[8]==player1:
        return 1
    elif board[6]==player1 and board[4]==player1 and board[2]==player1:
        return 1
    
    #Checking if player 2 won
    if board[0]==player2 and board[3]==player2 and board[6]==player2:
        return 2
    elif board[0]==player2 and board[1]==player2 and board[2]==player2:
        return 2
    elif board[2]==player2 and board[5]==player2 and board[8]==player2:
        return 2
    elif board[6]==player2 and board[7]==player2 and board[8]==player2:
        return 2
    elif board[6]==player2 and board[4]==player2 and board[2]==player2:
        return 2
    
    #Checking if we can countiue the game
    for i in board:
        if i=='': #No one won and there is space on the board
            return 0
    return 3 #There is no space on the board and no one won so we got a tie

#checking if the players want another game
def new_game():
    choice = input('Do you want another game (Y or N)? ')
    while choice not in ['Y','N']:
        choice = input('Please choose "Y" or "N ')
    return choice

print('Welcome to "Tic Tac Toe" game!')
gameStatus = 'Y'
while(gameStatus=='Y'):
    board =['','','','','','','','','']
    display(board)
    first = choose_first();
    player1,player2=choose_first();
    while(board_checking(player1, player2, board)==0):
        print('Player 1:')
        board = set_position_player(player1, board)
        display(board)
        if board_checking(player1, player2, board)==1 or board_checking(player1, player2, board)==3 :
            break
        print('player 2:')
        board = set_position_player(player2,board)
        display(board)
    result = board_checking(player1, player2, board)
    if result==3:
        print('TIE!')
    elif result==1:
        print('Player 1 won!')
    elif result==2:
        print('Player 2 won!')
    gameStatus=new_game()
print('Thank you for playing "Tic Tac Toe"!')
        
        
        
        
        
        
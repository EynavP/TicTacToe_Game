# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 12:32:03 2021

@author: eynavptia
""" 
import random


# Function to display the Tic Tac Toe board status
def display(board):
    print('\n'*10)
    print("  "+board[6]+" | "+board[7]+" | "+board[8]+" ")
    print("----------")
    print("  "+board[3]+" | "+board[4]+" | "+board[5]+" ")
    print("----------")
    print("  "+board[0]+" | "+board[1]+" | "+board[2]+" ")
   

#Randon the first to play
def choose_first():
    first = random.randint(0,1)
    if first == 0:
        player1 = marker('Player 1');
        if player1 == 'X':
            return ('X','O')
        else:
            return ('O','X')
    else:
        player2 = marker('Player 2');
        if player2 == 'X':
            return ('O','X')
        else:
            return ('X','O')

# Function to set the first player his marker
def marker(player):
    choice = input(f'{player} please choose "X" or "O" :')
    while choice!='X' and  choice!='O':
        choice = input(f'{player} please choose "X" or "O": ').upper()
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
    
    #Checking if player 1 won
    if ((board[0] == board[3] == board[6] == player1) or
        (board[0] == board[1] == board[2] == player1) or
        (board[2] == board[5] == board[8] == player1) or
        (board[6] == board[7] == board[8] == player1) or
        (board[6] == board[4] == board[2] ==player1) or
        (board[8] == board[4] == board[0]==player1)):
            return 1
    #Checking if player 2 won
    elif ((board[0] == board[3] == board[6] == player2) or
        (board[0] == board[1] == board[2] == player2) or
        (board[2] == board[5] == board[8] == player2) or
        (board[6] == board[7] == board[8] == player2) or
        (board[6] == board[4] == board[2] ==player2) or
        (board[8] == board[4] == board[0]==player2)):
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

#Main
print('Welcome to "Tic Tac Toe" game!')
gameStatus = 'Y'
while(gameStatus=='Y'):
    board =['']*9
    display(board)
    player1,player2=choose_first();
    while(board_checking(player1, player2, board)==0):
        print('Player 1:')
        board = set_position_player(player1, board)
        display(board)
        if board_checking(player1, player2, board)==1 or board_checking(player1, player2, board)==3 :
            break
        print('Player 2:')
        board = set_position_player(player2,board)
        display(board)
        if board_checking(player1, player2, board)==2 or board_checking(player1, player2, board)==3 :
            break
    result = board_checking(player1, player2, board)
    if result==3:
        print('TIE!')
    elif result==1:
        print('Player 1 won!')
    elif result==2:
        print('Player 2 won!')
    gameStatus=new_game()
print('Thank you for playing "Tic Tac Toe"!')
        
        
        
        
        
        
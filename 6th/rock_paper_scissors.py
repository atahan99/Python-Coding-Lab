"""
Author: Atahan Kucuk
Assignment: 06.2 - Rock Paper Scissors
Date: 10/18/2021

Description:
    It is an simple application that allows users to play rock paper scissors


"""
import random as r
#generating computer choice
def get_computer_choice():
    comp= ['rock', 'paper','scissors']
    return r.choice(comp)
#getting the user input
def get_player_choice():
    player = input('Choose rock, paper, or scissors: ')
    #validating user input
    while player == 'rock' or player == 'paper' or player =='scissors':
            return player
    else:
        print('You made an invalid choice. Please try again.')
        player = input('Choose rock, paper, or scissors: ')
        return player
#determing the winner
def get_winner(comp, player):
    status = ' '
    
    if comp == player:
        print('  Its a tie. Starting over.')
        status = 'tie'
    elif comp == 'paper' and player == 'rock':
        print('  paper beats rock')
        status = 'computer'
    elif comp == 'rock' and player == 'paper':
        print('  paper beats rock')
        status = 'player'
    elif comp == 'scissors' and player == 'paper':
        print('  scissors beats paper')
        status = 'computer'
    elif player == 'scissors' and comp == 'paper':
        print('  scissors beats paper')
        status = 'player'
    elif comp == 'rock' and player == 'scissors':
        print('  rock beats scissors')
        status = 'computer'
    elif player == 'rock' and comp == 'scissors':
        print('  rock beats scissors')
        status = 'player'
    return status

def main():
    #storing the choices
    comp = get_computer_choice()
    player = get_player_choice()
    print('  The computer chose '+comp+', and you chose '+player+'.')
    win = get_winner(comp,player)
    #comparing the chocies to determine who wins or who loose
    while win == 'tie':
        
        comp = get_computer_choice()
        player = get_player_choice()
        win = get_winner(comp,player)
        print('  The computer chose '+comp+', and you chose '+player+'.')
        if win == 'computer': 
            print('  You lost. Better luck next time.')
        if win == 'player':
            print('  You won the game!')
    print('Thanks for playing.')



if __name__ == '__main__':
    main()

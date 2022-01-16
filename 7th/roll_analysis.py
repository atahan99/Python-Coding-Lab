"""
Author: Atahan Kucuk
Assignment: 07.3 - Roll Analysis
Date: 10/31/2021

Description:
    This is an application that generates randim dice roll results


"""

import random as r
#getting a random number
def roll_d6():
    return r.randint(1,6)
#calculating 2 dice rolls
def get_2d6_rolls(n):
    dice_roll = []
    #calling the roll_d6 function
    for i in range(n):
        dice1 = roll_d6()
        dice2 = roll_d6()
        total = dice1 + dice2
        dice_roll.append(total)
    return dice_roll


def main():

    t = 1000000
    prob = []

    roll = get_2d6_rolls(t)
    #calculating the frequency 
    for i in range(11):
        prob.append(100*roll.count(i+2)/t)

    #printing out the output
    print('Roll  Frequency')
    for j in range(11):
        print(" ",format(j+2,'2'),"    ", format(prob[j],'5.2f'),"%", sep= "")



if __name__ == '__main__':
    main()

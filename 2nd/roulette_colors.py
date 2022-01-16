"""
Author: Atahan Kucuk
Assignment: 02.3 - Roulette Colors
Date: 09/18/2021

Description:
    This application is used to determine the color of the pockets depending on their number


"""


def main():
    #getting user input
    pocket = int(input('Please choose a pocket number: '))
    color = ' ' 
    #Determining the color of the pockets
    if pocket < 0 or pocket > 36 :
        print('  Invalid Input!')
    else : 
        if pocket == 0 :
            color = 'green.'
        if pocket >= 1 and pocket <=10 :
            if (pocket%2) == 0: 
                color = 'black.'
            if (pocket%2) != 0 : 
                color = 'red.'
        if pocket >= 11 and pocket <= 18 :
            if (pocket%2) == 0 :
                color = 'red.'
            if (pocket%2) != 0:
                color = 'black.'
        if pocket >= 19 and pocket <= 28 : 
            if (pocket%2) == 0 : 
                color = 'black.'
            if (pocket%2) != 0 :
                color = 'red.'
        if pocket >= 29  and pocket <= 36 :
            if (pocket%2) == 0 :
                color = 'red.'
            if (pocket%2) != 0 :
                color = 'black.' 
                #informing the user
        print(f'  Pocket number {pocket:.0f} is',color)

    
    
if __name__ == '__main__':
    main()

"""
Author: Atahan Kucuk
Assignment: 03.1 - Arrows
Date: 09/13/2021

Description:
    This is an application to draw a pattern of arrows depending on the user input for the count of the arrows


"""


def main():

#asking the user for arrow count
    amount = int(input('How many arrows should I draw? '))
 
 #drawing the arrow pattern
    for i in range(amount):
        msg = '<'
        msgf = ''
        for x in range(i): 
            msg = msg + '-'
        msgf = msg + '>'
        print(msgf)
 
    

if __name__ == '__main__':
    main()

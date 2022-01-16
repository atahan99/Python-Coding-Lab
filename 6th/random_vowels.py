"""
Author: Atahan Kuck
Assignment: 6.3 - Random Vowels
Date: 10/25/2021

Description:
    This is a python application that can be used to display random vowels drawed. 


"""

from turtle import *

# Import additional modules below this line.
import vowels
import random

# Write new functions below this line (starting with unit 4).


def start():
    """This function initializes the window and the turtle.
    Do not modify this function.
    """
    setup(600, 400)
    width(9)
    speed(0)
    penup()
    goto(-220, -30)


def main():
    """Write your mainline logic here."""
    #setting the start point 
    x = -300
    y = 100
    for i in range(5):
        r = random.randint(1,5)
        penup()
        goto(x,y)
        pendown()
    #displaying random vowels
        if r ==1:
            vowels.draw_a()
        elif r==2:
            vowels.draw_e()
        elif r==3:
            vowels.draw_i()
        elif r==4:
            vowels.draw_o()
        elif r==5:
            vowels.draw_u()
        x+=140


if __name__ == '__main__':
    # Do not change this part
    start()
    main()
    done()

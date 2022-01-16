
"""
Author: Atahan Kucuk
Assignment: 5.2 - Pentagon Spiral
Date: 10/11/2021

Description:
    an application to draw pentagon spirals


"""

from turtle import *

def start():
    """This function initializes the window and the turtle.
    Do not modify this function.
    """
    setup(564, 564)
    width(5)

def main():
    """Write your code below this line."""
    #loop to draw the pentagon spiral with increasing side lenghts
   
    for i in range(33):
        forward(8+(8*(i)))
        left(72)
        


# Do not change anything after this line.
if __name__ == '__main__':
    start()
    main()
    done()
